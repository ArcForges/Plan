# ArcForges delivery task prompts — Workers AI routing and metering

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Workers AI routing and metering

```text
Execute ArcForges delivery task AIR.00 — Provider adapters and routing (Workers AI).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-00).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/air-00 (python tools/delivery.py claim AIR.00 --worker <name>); task branch task/air-00 in AI; ledger record ledger/tasks/air-00.md.
Kind/size: service/L. Baseline: not-started.
Outcome: env.AI.run adapters exist for default/fast text, accepted image context, bge-m3 embedding and bge-reranker-base rerank; model availability/frozen-config/request-limits/tool-stream-shapes are validated before dispatch; C# records admission/routing/supplier version while CF executes the already-admitted intent.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.00

Entry condition: adoption slice ADOPT.08.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.10: published internal AI HTTP profile (model-intent/model-outcome/dispatch ports) from internal/ai-http/v1/schema.json
- [artifact] POL.08: active model/route policy snapshot naming the admitted catalogue subset
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AIR.09: actual normal published exact tokenizer/render/materializer implementation
- [integration] CON.36: actual published safe descriptor/artifact/pin and private model evidence
- [integration] CLOUD.13: actual current raw session/device/install and fixed descriptor materialization union
- [integration] CLOUD.75: actual privileged configured realm/recovery guard
- [integration] CLOUD.21: actual production signed executor/private bridge
- [integration] CLOUD.82: actual opaque same issuer/plan/scope family capabilities

Permitted write scope: AI:src/providers/workers-ai/**; AI:src/inference/**; AI:src/providers/workers-ai/** and src/inference/** (actual pinned raw=true GPT-OSS adapter executing the exact counted prompt/hash; preserve other original routing and acceptance obligations); AI:tests/model-input/** (actual generated private evidence/current route/raw prompt bytes, literal delimiters/unsupported arm/cancel/unknown dispatch components; no real inference in ordinaryCI); AI:src/model-input/** (only exact generated evidence/descriptor/rendered object slice materialization and full hash/owner/run/config crossbinding; no shadow tokenizer or heuristic count); AI:package.json and package-lock.json (only actual published CON36 mandatory proto closure and exact owned test registration; no toolchain/third-party changes); AI:eng/dependency-policy.* and eng/dependency-reviews/air-00-*.json and eng/provenance/** (only actual owned generated consumer/evaluated input/legal successors); Cloud:src/ArcForges.Cloud.Modules.Agent/ModelContext/** and AgentModule.cs (actual immutable existing descriptor projection/current bound source, public artifact read service and real owner factory); Cloud:src/ArcForges.Cloud.Modules.Abstractions/Agent/ModelContextPort.cs (required actual generated model context/current read/materialization owner ports; no Desktop Assistant types); Cloud:storage/plans/agent/model-context-*.sql (only actual existing descriptor row/current/lifecycle/immutable insert guards and read plans); Cloud:src/ArcForges.Cloud.Storage.D1/Physical/manifest/agent.json and Migrations/pending/agent__model-context-invariants.sql (only existing agent_model_descriptor closed original insertion/update/delete profile; preserve baseline0010 and price/tariff tables); Cloud:eng/verification/physical-schema.ts and tests/worker/d1-physical-schema.test.ts (only fixed agentModelDescriptorOriginal exact PK/config-model-purpose conflicts/immutable originals/newactive-retired lifecycle; no arbitrary SQL or shape waiver); Cloud:src/ArcForges.Cloud/Composition/ModelContextModule.cs and HostModules.cs (exact real Agent/Config/ModelInput factory registration; no module-private implementation import); Cloud:src/ArcForges.Cloud/PublicApi/Agent/** (only genuine generated ModelView7 and AgentService.ReadModelArtifact ingress with current raw C13/personal Workspace and strict complete shape/slice validation); Cloud:src/ArcForges.Cloud.Modules.Task/ModelInput/** and Modules.Chat/ModelInput/** (each owner actual immutable run input binding/guarded preparation/replay only; no crossmodule SQL); Cloud:src/ArcForges.Cloud.Storage.D1/Physical/manifest/task.json and chat.json and Migrations/pending/task__model-input-binding.sql and chat__model-input-binding.sql (only genuine each-owner run input sidecar with actual run FK/immutable descriptor-config-pin-render binding; no baseline edits or synthesized run ConfigVersion); Cloud:storage/plans/task/model-input-*.sql and chat/model-input-*.sql (only each owner immutable run binding insert/read/current guards); Cloud:worker/model-input/** (fixed protected encrypted render object parts/hash/owner/run/config bridge under unchanged private envelope; no workflow/log plaintext); Cloud:tests/ArcForges.Cloud.Tests/Agent/ModelContext/** and ModelInput/** and tests/worker/model-input*.test.ts (actual original descriptor/run sidecar replacement, current authority/pin/cap/buffer/cancel/unknown and exact provider bytes components); Cloud:Directory.Packages.props and exact owned Agent/host/tests csproj/packages.lock.json (only actual published ArcForges.AI.ModelInput and CON36 mandatory peer closure; no unrelated upgrade); Cloud:eng/provenance/files.json and policy/dependency-policy.json and dependency-reviews/air-00-*.json and tests/ArchitectureTests/EvaluatedRepositoryGate.cs (only actual owned source/consumer/API inputs and immutable reviewed successor); Cloud:src/ArcForges.Cloud.Storage.D1/Physical/PhysicalSchema.g.cs and PlanManifest.g.cs and worker/storage/plans.generated.ts (regenerate only actual admitted own source); Cloud:tests/worker/support/physical-rows.ts and tests/ArcForges.Cloud.Tests/Physical/PhysicalSchemaTests.cs (only legitimate correlated own descriptor/run binding fixtures and actual accepted-prefix table count; all constraints/search cap/negatives preserved); Cloud:eng/verification/physical-schema.ts (only fixed modelRunInputOriginal exact task_model_input_binding/chat_model_input_binding PK/ref insertion and immutable/delete invariants; preserve all other table profiles)
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (exclusive): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.; RES-private-configuration (append): Each owning task adds its own configuration section; activation is a signed publication by the policy lane; no task edits another section.
Unblocks: AIR.02, AIR.03, AIR.05, AIR.07, AIR.08, CLOUD.67, HAR.00, HAR.05, SRCH.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Actual selected model/capability-shape tests, withdrawn/unknown/unsupported request tests, request-size/output-bound tests, version-mismatch tests. Real CF calls only in the credentialed candidate gate, not ordinary CI (P2-017: no real AI inference in CI).
Completion evidence for the ledger: Routing decision, explainability and streaming results.
Notes: Narrow early risk proof: if env.AI.run cannot actually deliver the required capability shapes (tool/stream) as specified, the whole AI economics/product model is affected.

2026-10-07 approved model context and exact rendering producer repair (docs/decisions/approved-model-context-and-exact-rendering-producer-2026-10-07.md). Runtime coordinates the actual Agent-owned existing descriptor and Task/Chat-owned immutable run input witnesses, current Config source and exact raw provider dispatch. Each module retains own SQL and opaque capability. Counted GPT-OSS raw routes require exact current complete modelInputEvidence and immutable rendered object bytes/hash; unsupported templates/arms refuse before admission/debit, no hidden messages framing. Original all-route/image/embedding/rerank and actual provider acceptance remain. Fixed model-descriptor-materialization.commit-current joins genuine Agent record/Config approved current predicate/Platform75 under C13 sole union. No pure count/signed descriptor grants user permission.
```

```text
Execute ArcForges delivery task AIR.01 — Tariffs and cost dimensions.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/air-01 (python tools/delivery.py claim AIR.01 --worker <name>); task branch task/air-01 in Cloud; ledger record ledger/tasks/air-01.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Versioned tariffs with effective dates and the full cost-dimension set exist; each run locks a tariff snapshot at start; a historical charge is reconstructible from its locked snapshot; image-context units are metered separately from text units.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.01

Entry condition: adoption slice ADOPT.07.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] POL.02: the customerTariffs/supplierPrices keys in Private configuration.v1 and its signed activation mechanism
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Agent/Tariffs/**
Shared resources (follow the owner protocol): RES-private-configuration (append): Each owning task adds its own configuration section; activation is a signed publication by the policy lane; no task edits another section.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: AIR.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Rate-change immutability test, historical-explainability reconstruction test, per-dimension metering tests -- offline.
Completion evidence for the ledger: Rate-change immutability and historical explainability results.
```

```text
Execute ArcForges delivery task AIR.02 — Metering and settlement.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/air-02 (python tools/delivery.py claim AIR.02 --worker <name>); task branch task/air-02 in Cloud; ledger record ledger/tasks/air-02.md.
Kind/size: service/L. Baseline: not-started.
Outcome: C# reservation/intent commits before CF I/O, outcome receipt precedes settlement, attempt usage revisions are immutable; interactive runs and bounded inference jobs are both covered with stable attempt identity, supplier exposure, Run customer total and exact credit lots; unknown usage follows the deadline/liability ladder, never an automatic resend.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.02

Entry condition: adoption slice ADOPT.07.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.08: real budget/credit/admission ports (reservation, settlement transaction participants)
- [artifact] AIR.00: a dispatchable provider call to meter
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] COM.12: the real capacity admission participant

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Agent/Metering/**
Shared resources (follow the owner protocol): RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: AIR.04, AIR.06, AIR.08, HAR.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Actual CF normal/interrupted/lost outcome with concurrent duplicates and replayed receipts; cancelled/unknown hold sweep; tariff-change and operator-job isolation tests. Real-CF cases only at the credentialed candidate gate.
Completion evidence for the ledger: Metering accounting, idempotency, sweep and overdraft results.
```

```text
Execute ArcForges delivery task AIR.03 — Selected supplier and realm routing (no BYOK).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/air-03 (python tools/delivery.py claim AIR.03 --worker <name>); task branch task/air-03 in Cloud; ledger record ledger/tasks/air-03.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Only the Workers AI binding and explicit admitted catalogue route calls, with no AI Gateway/multiprovider bypass/fallback; self-host uses operator-owned credentials/funding with payment disabled by default; no silent substitution or credit crossing between official/self-host realms.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.03

Entry condition: adoption slice ADOPT.07.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AIR.00: the adapter's admitted-catalogue validation
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Agent/Routing/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.; RES-private-configuration (append): Each owning task adds its own configuration section; activation is a signed publication by the policy lane; no task edits another section.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: AIR.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Unavailable/withdrawn model, missing price/config, pre-dispatch-refusal-vs-unknown-dispatch, explicit-new-model-request tests -- offline.
Completion evidence for the ledger: No-BYOK structural assertions and credential-custody results.
```

```text
Execute ArcForges delivery task AIR.04 — Provider interaction records, redaction and cost transparency.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/air-04 (python tools/delivery.py claim AIR.04 --worker <name>); task branch task/air-04 in Cloud; ledger record ledger/tasks/air-04.md.
Kind/size: service/M. Baseline: not-started.
Outcome: A provider interaction record exists per call, separate from execution/capability/audit traces, carrying no content beyond policy; cost transparency surfaces show what a run cost and why.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.04 (interaction record, redaction, and cost-transparency surfaces (Cloud side)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.04

Entry condition: adoption slice ADOPT.07.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AIR.02: metered attempts to record interactions against
- [artifact] CLOUD.69: the Cloud-side correlation seam for the provider interaction record
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Agent/InteractionRecords/**
Shared resources (follow the owner protocol): RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: AIR.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Trace-separation test; content-redaction test; cost-explainability test -- offline.
Completion evidence for the ledger: Trace separation, redaction and cost explainability results.
Notes: Planning repair 2026-10-05: every provider interaction record carries the call's correlation identity and the provider request identifier (CR-05) through the CLOUD.69 seam; this is part of this task's own acceptance and of the real provider hop that PLT.48's correlation scenario names as a later owner (no new write scope).
```

```text
Execute ArcForges delivery task AIR.05 — Content-origin marking at the provider generation boundary.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/air-05 (python tools/delivery.py claim AIR.05 --worker <name>); task branch task/air-05 in AI; ledger record ledger/tasks/air-05.md.
Kind/size: service/M. Baseline: not-started.
Outcome: The frozen content-origin profile is implemented at the point AI-generated content is produced; every artifact type carries the required transparency marking; malformed/hash-mismatched marks and marking retry are handled; this satisfies VG-01 once the regime determination is recorded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.04 (transparency marking mechanism at the provider generation boundary; marking-coverage per artifact type): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.04

Entry condition: adoption slice ADOPT.08.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AIR.00: generated model output to mark
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: AI:src/providers/workers-ai/ContentOrigin/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.
Unblocks: AIR.90, HAR.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Real provider text through durable output and downstream carrier fixtures; deterministic/non-AI and legacy controls; malformed/hash-mismatched mark; marking retry -- offline against fixture carriers, real text only at the AIR.08 credentialed gate.
Completion evidence for the ledger: Marking-coverage results per artifact type; carrier/propagation/failure vectors with payload and manifest hashes.
Notes: HAR.03 (WP-52.03 durable output) consumes this task's ContentOrigin carrier as a start artifact -- internal the AI lanes cross-reference.
```

```text
Execute ArcForges delivery task AIR.06 — Funding and uncertain-outcome proof.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/air-06 (python tools/delivery.py claim AIR.06 --worker <name>); task branch task/air-06 in Cloud; ledger record ledger/tasks/air-06.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Supplier intent/exposure and customer settlement are proven independent: Brave search is operator-funded while processing results is customer inference; a crash before/after dispatch, an unknown deadline, and late usage after a closed no-later-debit window are all handled without an automatic model retry.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.05

Entry condition: adoption slice ADOPT.07.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AIR.02: the reservation/settlement engine to prove uncertainty handling against
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Agent/Metering/UncertainOutcome/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: AIR.90, HAR.04, SRCH.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Search-without-customer-debit, model-debit-once, crash-before/after-dispatch, unknown-deadline, late-usage-after-closed, no-automatic-retry tests -- offline with real-CF-shaped fixtures; real dispatch only at AIR.08's gate.
Completion evidence for the ledger: Degradation, reservation-release and alert results.
Notes: HAR.04 (WP-52.04 general effect-certainty classification) treats this task's ledger pattern as its worked precedent -- internal the AI lanes cross-reference.
```

```text
Execute ArcForges delivery task AIR.07 — Provider test-environment coverage.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/air-07 (python tools/delivery.py claim AIR.07 --worker <name>); task branch task/air-07 in AI; ledger record ledger/tasks/air-07.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Every provider integration is exercised against the provider's own test environment, with its contract shape frozen as recorded fixtures so ordinary CI never depends on provider availability.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.06

Entry condition: adoption slice ADOPT.08.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AIR.00: the adapter to exercise against the test environment
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: AI:tests/provider-fixtures/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.
Unblocks: AIR.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Per-provider test-environment run (credentialed, not ordinary CI); fixture-driven CI run with the provider deliberately unreachable, per P2-017.
Completion evidence for the ledger: Per-provider test-environment runs and fixture-driven CI results -- PG-10.
```

```text
Execute ArcForges delivery task AIR.08 — Real-provider metering evidence and stubbed-path removal.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/air-08 (python tools/delivery.py claim AIR.08 --worker <name>); task branch task/air-08 in AI; ledger record ledger/tasks/air-08.md.
Kind/size: integration/L. Baseline: not-started.
Outcome: Actual Workers AI responses for each selected capability are recorded and normalized into independent sanitized fixtures; deterministic fixtures run on ordinary CI while the credentialed real-CF candidate gate proves exact Worker/model/config identity; the WP-17.05 stubbed managed provider path is retired.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.07 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.07

Entry condition: adoption slice ADOPT.08.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AIR.00: the real adapter to record responses from
- [artifact] AIR.02: the real settlement engine to reconcile the recorded evidence through
- [artifact] AST.15: assistant admission path that carried the stubbed provider
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: AI:tests/provider-fixtures/**; Cloud:tests/Cloud.Tests.Integration/AiMetering/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.
Permitted substitutes (never real integration evidence): SUB-stubbed-provider-path: early client/UI development against a scripted AI response only Real producer ['AIR.00']; removed by AIR.08
Unblocks: AIR.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Model response drift, missing category, cumulative stream, embedding/rerank result validation tests offline; controlled real-provider run at the credentialed candidate gate only.
Completion evidence for the ledger: Real-provider normalisation, settlement and worked-fixture results -- PG-13.
Notes: This task is the structural replacement named in implementation-sequence.md Sec.3.1: 'Stubbed managed provider path (WP-17.05)... Deleted by WP-43.00, WP-43.07' -- AIR.00 builds the real path, AIR.08 proves and removes the stub.
```

```text
Execute ArcForges delivery task AIR.90 — Verify owned artifact and real integration (AI routing and metering).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-90).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/air-90 (python tools/delivery.py claim AIR.90 --worker <name>); task branch task/air-90 in Cloud; ledger record ledger/tasks/air-90.md.
Kind/size: service/M. Baseline: not-started.
Outcome: All AIR deliverables assemble under the selected repository/package/runtime/protocol authorities with the frozen Workers AI model subset, capability matrix, normalization and known/unknown usage contract proven; Gateway is confirmed not a required dependency.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.90 (remaining aggregation/receipt): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.90
- WP-43:p2-010-required-behavior-and-closure-rea P2-010 required behavior and closure: real ExecutionOwner task/turn + operator-funded compaction/search support, durable receipts vs temporary bodies outside D1/SQLite/backups/checkpoints (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, package-level obligation

Entry condition: adoption slice ADOPT.07.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AIR.08: real-provider evidence
- [artifact] AIR.01: package task delivered
- [artifact] AIR.03: package task delivered
- [artifact] AIR.04: package task delivered
- [artifact] AIR.05: package task delivered
- [artifact] AIR.06: package task delivered
- [artifact] AIR.07: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:tests/Cloud.Tests.Integration/AiMetering/**
Shared resources (follow the owner protocol): RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: REL.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Real selected model/tool/embedding cases and provider refusal/lost-result/usage reconciliation tied to C# admitted call and config identity; P2-017 proportionate.
Completion evidence for the ledger: Owned artifact and real-integration receipt: source commit, producer version, candidate hashes, actual runtime/provider, scenario, result, real-vs-fixture status.
Notes: Also carries the P2-010 package closure text (real ExecutionOwner task/turn + operator-funded compaction/search support; durable receipts vs temporary bodies kept outside D1/SQLite history, backups and Workflow checkpoints).
```

```text
Execute ArcForges delivery task AIR.09 — Complete pinned tokenizer, rendering and model input producer.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/air-09 (python tools/delivery.py claim AIR.09 --worker <name>); task branch task/air-09 in DesktopPlatform; ledger record ledger/tasks/air-09.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Normally publish ArcForges.AI.ModelInput complete pure supported o200k/Harmony tokenizer/render/materializer and semantic bundle validator with exact actual verified artifacts, immutable generated descriptor/pin inputs, original-source spans/token IDs/costs and faithful bounded rendered provider bytes. No approximate count, constructor permission, default unknown template or whole configuration/harness cycle.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.00 (minimum actual independent model tokenizer/render/materializer producer; original AIR00 routing/provider acceptance retained): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.00

Entry condition: adoption slice ADOPT.08.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CON.10: actual published complete content/profile/skill/tool records
- [artifact] CON.11: actual published transcript/source/turn input records
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CON.36: actual normal published descriptor/bundle/pin and model-bound helper source

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.AI.ModelInput/** (new real pure engine/materializer/validator/captured operational inputs/API/README/project/lock; no Cloud or Desktop Assistant reference); DesktopPlatform:tests/ModelInputTests/** (new genuine independent official tokenizer token-ID/render-byte/count/classifier/span/material/limit/cancel/disposal and unsupported-arm components); DesktopPlatform:eng/model-input/** and fixtures/model-input/** (owned exact pinned source/UCD data legal/provenance acquisition recipe and independently authored official tokenizer goldens; no production self-test authority); DesktopPlatform:DesktopPlatform.slnx (append only actual ModelInput and owning component test projects); DesktopPlatform:Directory.Packages.props and exact ModelInput/tests packages.lock.json (only actual published Foundation/CON36 Validation mandatory same-release peers and existing admitted test closure); DesktopPlatform:eng/packaging/packages.json (only new real verified ArcForges.AI.ModelInput managed package/dependencies/legal assets); DesktopPlatform:eng/policy/architecture-projects.json and licence-boundary.json (only actual owned producer/test classification); DesktopPlatform:eng/policy/architecture-contract-tests.json and architecture-evidence.json (only actual owned API/direct behavior evidence mappings); DesktopPlatform:eng/policy/reconciliation/active-projects.json and project-updates.json (only actual owned new project blobs and immutable input successors); DesktopPlatform:eng/policy/dependency-policy.json and dependency-reviews/air-09-*.json and eng/provenance/** and NOTICE.md (only actual owned producer/data/legal/evaluated input immutable successors); DesktopPlatform:.github/workflows/pr-gate.yml and package-validation.yml (only actual owned ordinary component/producer registration, preserve all existing triggers/gates/toolchain); DesktopPlatform:docs/model-input-producer.md (actual artifact/classifier/BPE/render/API/profile/bounds/legal and consumer obligations)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.; RES-contract-consumer-pins (append): A consumer task updates the pin it needs through a reviewed dependency change to the exact published candidate containing its closure; no consumer pins an unpublished closure or references Contracts source.
Unblocks: AIR.00, AST.01, HAR.01, POL.02

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Independently pinned official token IDs/counts/UTF8 rendering and complete Unicode17 scalar tables, all actual artifact hashes/category/pattern/BPE ties/span provenance, signed0 semantic legacy invariance, literal Harmony delimiters/control/astral/U2028/unpaired input, actual tool/context/resource unsupported arms, finite work/admission/cancellation/ignored callback/shutdown/key-buffer disposal. No live provider in ordinary CI; real consumer/provider acceptance remains original AIR00/HAR01/AST ownership.
Completion evidence for the ledger: Exact independently reviewed source/data/legal/input identities, actual direct components and applicable Windows/Linux CI, real normal managed package publication and safe captured API. Pure success is not Config readiness, current permission or provider acceptance.
Notes: 2026-10-07 approved model context and exact rendering producer repair (docs/decisions/approved-model-context-and-exact-rendering-producer-2026-10-07.md). Runtime worker w-codex-20261006-runtime owns the real pure producer. Independent package output allows Config Stage and client/server adapters to join without whole-task completion cycle; all consumer current authority and actual acceptance remain separate.
```
