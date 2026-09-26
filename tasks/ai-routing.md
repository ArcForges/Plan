# ArcForges delivery task prompts — Workers AI routing and metering

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Workers AI routing and metering

```text
Execute ArcForges delivery task AIR.00 — Provider adapters and routing (Workers AI).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-00).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/air-00 (python tools/delivery.py claim AIR.00 --worker <name>); task branch task/air-00 in AI; ledger record ledger/tasks/air-00.md.
Kind/size: service/L. Baseline: not-started.
Outcome: env.AI.run adapters exist for default/fast text, accepted image context, bge-m3 embedding, bge-reranker-base rerank and slate.transcribe.v1 Whisper ASR; model availability/frozen-config/request-limits/tool-stream-shapes are validated before dispatch; C# records admission/routing/supplier version while CF executes the already-admitted intent.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.00

Entry condition: adoption slice ADOPT.08.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.10: published internal AI HTTP profile (model-intent/model-outcome/dispatch ports) from internal/ai-http/v1/schema.json
- [artifact] POL.08: active model/route policy snapshot naming the admitted catalogue subset
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: AI:src/providers/workers-ai/**; AI:src/inference/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (exclusive): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.; RES-private-configuration (append): Each owning task adds its own configuration section; activation is a signed publication by the policy lane; no task edits another section.
Unblocks: AIR.02, AIR.03, AIR.05, AIR.07, AIR.08, AIR.09, CLOUD.67, HAR.00, HAR.05, SRCH.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Actual selected model/capability-shape tests, withdrawn/unknown/unsupported request tests, request-size/output-bound tests, version-mismatch tests. Real CF calls only in the credentialed candidate gate, not ordinary CI (P2-017: no real AI inference in CI).
Completion evidence for the ledger: Routing decision, explainability and streaming results.
Notes: Narrow early risk proof: if env.AI.run cannot actually deliver the required capability shapes (tool/stream, ASR) as specified, the whole AI economics/product model is affected.
```

```text
Execute ArcForges delivery task AIR.01 — Tariffs and cost dimensions.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/air-01 (python tools/delivery.py claim AIR.01 --worker <name>); task branch task/air-01 in Cloud; ledger record ledger/tasks/air-01.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Versioned tariffs with effective dates and the full cost-dimension set exist; each run locks a tariff snapshot at start; a historical charge is reconstructible from its locked snapshot; media units are metered separately from text units.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.01

Entry condition: adoption slice ADOPT.07.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] POL.02: the customerTariffs/supplierPrices keys in Private configuration.v1 and its signed activation mechanism
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Agent/Tariffs/**
Shared resources (follow the owner protocol): RES-private-configuration (append): Each owning task adds its own configuration section; activation is a signed publication by the policy lane; no task edits another section.
Unblocks: AIR.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Rate-change immutability test, historical-explainability reconstruction test, per-dimension metering tests -- offline.
Completion evidence for the ledger: Rate-change immutability and historical explainability results.
```

```text
Execute ArcForges delivery task AIR.02 — Metering and settlement.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/air-02 (python tools/delivery.py claim AIR.02 --worker <name>); task branch task/air-02 in Cloud; ledger record ledger/tasks/air-02.md.
Kind/size: service/L. Baseline: not-started.
Outcome: C# reservation/intent commits before CF I/O, outcome receipt precedes settlement, attempt usage revisions are immutable; interactive runs and bounded inference jobs are both covered with stable attempt identity, supplier exposure, Run customer total and exact credit lots; unknown usage follows the deadline/liability ladder, never an automatic resend.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.02

Entry condition: adoption slice ADOPT.07.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.08: real budget/credit/admission ports (reservation, settlement transaction participants)
- [artifact] AIR.00: a dispatchable provider call to meter
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] COM.12: the real capacity admission participant

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Agent/Metering/**
Unblocks: AIR.04, AIR.06, AIR.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Actual CF normal/interrupted/lost outcome with concurrent duplicates and replayed receipts; cancelled/unknown hold sweep; tariff-change and operator-job isolation tests. Real-CF cases only at the credentialed candidate gate.
Completion evidence for the ledger: Metering accounting, idempotency, sweep and overdraft results.
```

```text
Execute ArcForges delivery task AIR.03 — Selected supplier and realm routing (no BYOK).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/air-03 (python tools/delivery.py claim AIR.03 --worker <name>); task branch task/air-03 in Cloud; ledger record ledger/tasks/air-03.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Only the Workers AI binding and explicit admitted catalogue route calls, with no AI Gateway/multiprovider bypass/fallback; self-host uses operator-owned credentials/funding with payment disabled by default; no silent substitution or credit crossing between official/self-host realms.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.03

Entry condition: adoption slice ADOPT.07.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AIR.00: the adapter's admitted-catalogue validation
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Agent/Routing/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.; RES-private-configuration (append): Each owning task adds its own configuration section; activation is a signed publication by the policy lane; no task edits another section.
Unblocks: AIR.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Unavailable/withdrawn model, missing price/config, pre-dispatch-refusal-vs-unknown-dispatch, explicit-new-model-request tests -- offline.
Completion evidence for the ledger: No-BYOK structural assertions and credential-custody results.
```

```text
Execute ArcForges delivery task AIR.04 — Provider interaction records, redaction and cost transparency.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/air-04 (python tools/delivery.py claim AIR.04 --worker <name>); task branch task/air-04 in Cloud; ledger record ledger/tasks/air-04.md.
Kind/size: service/M. Baseline: not-started.
Outcome: A provider interaction record exists per call, separate from execution/capability/audit traces, carrying no content beyond policy; cost transparency surfaces show what a run cost and why.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.04 (interaction record, redaction, and cost-transparency surfaces (Cloud side)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.04

Entry condition: adoption slice ADOPT.07.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AIR.02: metered attempts to record interactions against
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Agent/InteractionRecords/**
Unblocks: AIR.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Trace-separation test; content-redaction test; cost-explainability test -- offline.
Completion evidence for the ledger: Trace separation, redaction and cost explainability results.
```

```text
Execute ArcForges delivery task AIR.05 — Content-origin marking at the provider generation boundary.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/air-05 (python tools/delivery.py claim AIR.05 --worker <name>); task branch task/air-05 in AI; ledger record ledger/tasks/air-05.md.
Kind/size: service/M. Baseline: not-started.
Outcome: The frozen content-origin profile is implemented at the point AI-generated content is produced; every artifact type carries the required transparency marking; malformed/hash-mismatched marks and marking retry are handled; this satisfies VG-01 once the regime determination is recorded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.04 (transparency marking mechanism at the provider generation boundary; marking-coverage per artifact type): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.04

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

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/air-06 (python tools/delivery.py claim AIR.06 --worker <name>); task branch task/air-06 in Cloud; ledger record ledger/tasks/air-06.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Supplier intent/exposure and customer settlement are proven independent: Brave search is operator-funded while processing results is customer inference; a crash before/after dispatch, an unknown deadline, and late usage after a closed no-later-debit window are all handled without an automatic model retry.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.05

Entry condition: adoption slice ADOPT.07.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AIR.02: the reservation/settlement engine to prove uncertainty handling against
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Agent/Metering/UncertainOutcome/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.
Unblocks: AIR.90, HAR.04, SRCH.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Search-without-customer-debit, model-debit-once, crash-before/after-dispatch, unknown-deadline, late-usage-after-closed, no-automatic-retry tests -- offline with real-CF-shaped fixtures; real dispatch only at AIR.08's gate.
Completion evidence for the ledger: Degradation, reservation-release and alert results.
Notes: HAR.04 (WP-52.04 general effect-certainty classification) treats this task's ledger pattern as its worked precedent -- internal the AI lanes cross-reference.
```

```text
Execute ArcForges delivery task AIR.07 — Provider test-environment coverage.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/air-07 (python tools/delivery.py claim AIR.07 --worker <name>); task branch task/air-07 in AI; ledger record ledger/tasks/air-07.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Every provider integration is exercised against the provider's own test environment, with its contract shape frozen as recorded fixtures so ordinary CI never depends on provider availability.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.06

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

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/air-08 (python tools/delivery.py claim AIR.08 --worker <name>); task branch task/air-08 in AI; ledger record ledger/tasks/air-08.md.
Kind/size: integration/L. Baseline: not-started.
Outcome: Actual Workers AI responses for each selected capability are recorded and normalized into independent sanitized fixtures; deterministic fixtures run on ordinary CI while the credentialed real-CF candidate gate proves exact Worker/model/config identity; the WP-17.05 stubbed managed provider path is retired.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.07

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
Unblocks: AIR.90, HAR.91

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Model response drift, missing category, cumulative stream, embedding/rerank result validation tests offline; controlled real-provider run at the credentialed candidate gate only.
Completion evidence for the ledger: Real-provider normalisation, settlement and worked-fixture results -- PG-13.
Notes: This task is the structural replacement named in implementation-sequence.md Sec.3.1: 'Stubbed managed provider path (WP-17.05)... Deleted by WP-43.00, WP-43.07' -- AIR.00 builds the real path, AIR.08 proves and removes the stub.
```

```text
Execute ArcForges delivery task AIR.09 — ASR/Whisper capability closure and inference-late-outcome reconciliation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/air-09 (python tools/delivery.py claim AIR.09 --worker <name>); task branch task/air-09 in AI; ledger record ledger/tasks/air-09.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Real Workers AI Whisper ASR is proven through typed audio manifests and service object grants with metering verified against the actual response/manifest; inference-late-outcome reconciliation is evidence-only; bounded Workflow limits hold; a stale result can never publish or charge the customer.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.90 (the final-review closure paragraph: real Workers AI Whisper with typed audio manifests/service object grants, supplier metering against actual response/manifest with missing usage retained uncertain, inference-late-outcome evidence-only reconciliation, bounded Workflow limits, stale-result non-publication): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.90
- WP-43:final-review-closure-paragraph-real-whis Final-review closure paragraph: real Whisper/typed audio manifests, inference-late-outcome reconciliation, bounded Workflow limits, stale-result non-publication (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, package-level obligation

Entry condition: adoption slice ADOPT.08.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AIR.00: the slate.transcribe.v1 Whisper adapter and the separate lightweight InferenceWorkflow
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: AI:src/inference/Asr/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.
Unblocks: AIR.90, HAR.91

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Real Whisper run at the credentialed gate with synthetic/generic audio fixtures (this task proves the capability, not the Slate product scenario); bounded-limits and stale-result tests offline.
Completion evidence for the ledger: Supplier metering vs actual response/manifest; inference-late-outcome reconciliation evidence.
Notes: Deliberately distinguished from WP-52.06's Slate closure paragraph: this task proves the ASR provider capability generically with synthetic audio; HAR's IM.slate-transcription-adoption proves the real Slate end-to-end scenario and is the only piece of this area that genuinely needs WP-39.
```

```text
Execute ArcForges delivery task AIR.90 — Verify owned artifact and real integration (AI routing and metering).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\ai-routing.md (anchor task-air-90).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/air-90 (python tools/delivery.py claim AIR.90 --worker <name>); task branch task/air-90 in Cloud; ledger record ledger/tasks/air-90.md.
Kind/size: service/M. Baseline: not-started.
Outcome: All AIR deliverables assemble under the selected repository/package/runtime/protocol authorities with the frozen Workers AI model subset, capability matrix, normalization and known/unknown usage contract proven; Gateway is confirmed not a required dependency.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-43.90 (remaining aggregation/receipt): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, anchor rule-wp-43.90
- WP-43:p2-010-required-behavior-and-closure-rea P2-010 required behavior and closure: real ExecutionOwner task/turn + operator-funded compaction/search support, durable receipts vs temporary bodies outside D1/SQLite/backups/checkpoints (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\43-managed-ai-routing-and-metering.md, package-level obligation

Entry condition: adoption slice ADOPT.07.ai-routing is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AIR.08: real-provider evidence
- [artifact] AIR.01: package task delivered
- [artifact] AIR.03: package task delivered
- [artifact] AIR.04: package task delivered
- [artifact] AIR.05: package task delivered
- [artifact] AIR.06: package task delivered
- [artifact] AIR.07: package task delivered
- [artifact] AIR.09: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:tests/Cloud.Tests.Integration/AiMetering/**
Unblocks: REL.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Real selected model/tool/embedding cases and provider refusal/lost-result/usage reconciliation tied to C# admitted call and config identity; P2-017 proportionate.
Completion evidence for the ledger: Owned artifact and real-integration receipt: source commit, producer version, candidate hashes, actual runtime/provider, scenario, result, real-vs-fixture status.
Notes: Also carries the P2-010 package closure text (real ExecutionOwner task/turn + operator-funded compaction/search support; durable receipts vs temporary bodies kept outside D1/SQLite history, backups and Workflow checkpoints).
```
