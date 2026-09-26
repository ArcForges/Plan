# ArcForges delivery task prompts — Adoption stage

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Adoption stage

```text
Execute ArcForges delivery task ADOPT.01 — Freeze the adoption baseline.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\Plan-B (integration owner: Plan integration owner, the holder of roles/integration-plan).
Claim and handoff record: claims/adopt-01 (python tools/delivery.py claim ADOPT.01 --worker <name>); task branch task/adopt-01 in Plan; ledger record ledger/tasks/adopt-01.md.
Kind/size: adoption/S. Baseline: not-started.
Outcome: The Plan ledger records, for every repository, the main head, open pull requests and branches and the latest published candidate per registry, so every adoption slice starts from the same frozen inputs. The baseline is complete through WP-03.02; WP-03.03 has not started.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- P2-018 (adoption stage: baseline inputs): C:\MyFile\Projects\ArcForges-Design-B\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-018

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Plan:ledger/adoption/baseline.md; Plan:ledger/README.md
Unblocks: ADOPT.02, ADOPT.02.app-composition, ADOPT.02.assistant, ADOPT.02.cloud, ADOPT.02.device-bridge, ADOPT.02.execution, ADOPT.02.extensions, ADOPT.02.foundation, ADOPT.02.governance, ADOPT.02.native, ADOPT.02.platform, ADOPT.02.policy, ADOPT.02.release, ADOPT.02.runtime-proofs, ADOPT.02.updater, ADOPT.03, ADOPT.03.contracts, ADOPT.03.extensions, ADOPT.03.governance, ADOPT.03.release, ADOPT.04, ADOPT.04.app-composition, ADOPT.04.arcnotes, ADOPT.04.governance, ADOPT.04.release, ADOPT.04.runtime-proofs, ADOPT.05, ADOPT.05.arcscope, ADOPT.05.governance, ADOPT.05.release, ADOPT.05.runtime-proofs, ADOPT.05.simulator, ADOPT.06, ADOPT.06.arcslate, ADOPT.06.governance, ADOPT.06.release, ADOPT.06.runtime-proofs, ADOPT.07, ADOPT.07.ai-routing, ADOPT.07.cloud, ADOPT.07.commerce, ADOPT.07.device-bridge, ADOPT.07.extensions, ADOPT.07.governance, ADOPT.07.harness, ADOPT.07.operations, ADOPT.07.policy, ADOPT.07.release, ADOPT.07.runtime-proofs, ADOPT.07.search, ADOPT.07.simulator, ADOPT.08, ADOPT.08.ai-routing, ADOPT.08.extensions, ADOPT.08.governance, ADOPT.08.harness, ADOPT.09, ADOPT.09.governance, ADOPT.09.operations, ADOPT.09.release, ADOPT.09.runtime-proofs, ADOPT.09.web, ADOPT.10, ADOPT.10.android, ADOPT.10.governance, ADOPT.10.release, ADOPT.10.runtime-proofs, ADOPT.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Read-only inspection of repositories, pull requests and registry receipts already recorded; no builds, downloads or runtime checks (P2-017).
Completion evidence for the ledger: Baseline record with exact commit identities per repository, open pull request list and latest candidate identities; reviewed and merged in the Plan repository.
```

```text
Execute ArcForges delivery task ADOPT.02 — Adopt DesktopPlatform.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/adopt-02 (python tools/delivery.py claim ADOPT.02 --worker <name>); task branch task/adopt-02 in Plan; ledger record ledger/tasks/adopt-02.md.
Kind/size: adoption/S. Baseline: not-started.
Outcome: The repository-wide adoption facts for DesktopPlatform (main head, retained CI workflow inventory under P2-017, package identities and pins, shared roots and source inventory) are recorded once for its slices to cite, and the DesktopPlatform classification table is complete when every adoption slice of the repository is complete. The governance slice schedules the replacement of the design-policy graph check that still validates the retired work-package graph.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- P2-018 (adoption stage: DesktopPlatform repository record): C:\MyFile\Projects\ArcForges-Design-B\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-018

Adoption slices (claim, review and record each separately as ledger/tasks/<slice key>.md, for example ledger/tasks/adopt-02-app-composition.md, plus one ledger/tasks/<key>.md with status inherited per task it classifies as inherited; one pull request may carry several; each slice opens only its own repository lane; each has its own prompt under "Adoption slices" below):
- ADOPT.02.app-composition: Adopt DesktopPlatform: Application composition (opens 6 tasks)
- ADOPT.02.assistant: Adopt DesktopPlatform: Embedded assistant (opens 22 tasks)
- ADOPT.02.cloud: Adopt DesktopPlatform: Cloud core (opens 2 tasks)
- ADOPT.02.device-bridge: Adopt DesktopPlatform: Application presence and tool bridge (opens 3 tasks)
- ADOPT.02.execution: Adopt DesktopPlatform: Execution engine (opens 9 tasks)
- ADOPT.02.extensions: Adopt DesktopPlatform: Extension platform and integrations (opens 7 tasks)
- ADOPT.02.foundation: Adopt DesktopPlatform: Foundation values (opens 7 tasks)
- ADOPT.02.governance: Adopt DesktopPlatform: Family governance and policy tests (opens 4 tasks; records 3 accepted tasks as inherited)
- ADOPT.02.native: Adopt DesktopPlatform: Native producers and probes (opens 25 tasks)
- ADOPT.02.platform: Adopt DesktopPlatform: Desktop platform mechanisms (opens 56 tasks)
- ADOPT.02.policy: Adopt DesktopPlatform: Dynamic policy and configuration (opens 1 task)
- ADOPT.02.release: Adopt DesktopPlatform: Release readiness and family release (opens 2 tasks)
- ADOPT.02.runtime-proofs: Adopt DesktopPlatform: Runtime proofs (opens 4 tasks)
- ADOPT.02.updater: Adopt DesktopPlatform: Desktop distribution and update (opens 8 tasks)

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] ADOPT.01: frozen baseline record
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] ADOPT.02.app-composition: slice recorded
- [integration] ADOPT.02.assistant: slice recorded
- [integration] ADOPT.02.cloud: slice recorded
- [integration] ADOPT.02.device-bridge: slice recorded
- [integration] ADOPT.02.execution: slice recorded
- [integration] ADOPT.02.extensions: slice recorded
- [integration] ADOPT.02.foundation: slice recorded
- [integration] ADOPT.02.governance: slice recorded
- [integration] ADOPT.02.native: slice recorded
- [integration] ADOPT.02.platform: slice recorded
- [integration] ADOPT.02.policy: slice recorded
- [integration] ADOPT.02.release: slice recorded
- [integration] ADOPT.02.runtime-proofs: slice recorded
- [integration] ADOPT.02.updater: slice recorded

Permitted write scope: Plan:ledger/adoption/DesktopPlatform.md; Plan:ledger/tasks/adopt-02.md

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Review of merged source, retained CI results and receipts only; no new builds, downloads or runtime checks (P2-017).
Completion evidence for the ledger: Repository adoption record with the repository-wide facts, links to every slice record, the combined classification table and any conflicts raised under D-001.
```

```text
Execute ArcForges delivery task ADOPT.03 — Adopt Contracts.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/adopt-03 (python tools/delivery.py claim ADOPT.03 --worker <name>); task branch task/adopt-03 in Plan; ledger record ledger/tasks/adopt-03.md.
Kind/size: adoption/S. Baseline: not-started.
Outcome: The repository-wide adoption facts for Contracts (main head, retained CI workflow inventory under P2-017, package identities and pins, shared roots and source inventory) are recorded once for its slices to cite, and the Contracts classification table is complete when every adoption slice of the repository is complete. The accepted WP-03.00 to WP-03.02 receipts are recorded as inherited by the contracts slice; every later Contracts task, starting with the WP-03.03 closures, is open.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- P2-018 (adoption stage: Contracts repository record): C:\MyFile\Projects\ArcForges-Design-B\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-018

Adoption slices (claim, review and record each separately as ledger/tasks/<slice key>.md, for example ledger/tasks/adopt-03-contracts.md, plus one ledger/tasks/<key>.md with status inherited per task it classifies as inherited; one pull request may carry several; each slice opens only its own repository lane; each has its own prompt under "Adoption slices" below):
- ADOPT.03.contracts: Adopt Contracts: Contracts schema closures (opens 22 tasks; records 3 accepted tasks as inherited)
- ADOPT.03.extensions: Adopt Contracts: Extension platform and integrations (opens 3 tasks)
- ADOPT.03.governance: Adopt Contracts: Family governance and policy tests (opens 2 tasks)
- ADOPT.03.release: Adopt Contracts: Release readiness and family release (opens 1 task)

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] ADOPT.01: frozen baseline record
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] ADOPT.03.contracts: slice recorded
- [integration] ADOPT.03.extensions: slice recorded
- [integration] ADOPT.03.governance: slice recorded
- [integration] ADOPT.03.release: slice recorded

Permitted write scope: Plan:ledger/adoption/Contracts.md; Plan:ledger/tasks/adopt-03.md

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Review of merged source, retained CI results and receipts only; no new builds, downloads or runtime checks (P2-017).
Completion evidence for the ledger: Repository adoption record with the repository-wide facts, links to every slice record, the combined classification table and any conflicts raised under D-001.
```

```text
Execute ArcForges delivery task ADOPT.04 — Adopt ArcNotes.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/adopt-04 (python tools/delivery.py claim ADOPT.04 --worker <name>); task branch task/adopt-04 in Plan; ledger record ledger/tasks/adopt-04.md.
Kind/size: adoption/S. Baseline: not-started.
Outcome: The repository-wide adoption facts for ArcNotes (main head, retained CI workflow inventory under P2-017, package identities and pins, shared roots and source inventory) are recorded once for its slices to cite, and the ArcNotes classification table is complete when every adoption slice of the repository is complete.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- P2-018 (adoption stage: ArcNotes repository record): C:\MyFile\Projects\ArcForges-Design-B\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-018

Adoption slices (claim, review and record each separately as ledger/tasks/<slice key>.md, for example ledger/tasks/adopt-04-app-composition.md, plus one ledger/tasks/<key>.md with status inherited per task it classifies as inherited; one pull request may carry several; each slice opens only its own repository lane; each has its own prompt under "Adoption slices" below):
- ADOPT.04.app-composition: Adopt ArcNotes: Application composition (opens 2 tasks)
- ADOPT.04.arcnotes: Adopt ArcNotes: ArcNotes (opens 35 tasks)
- ADOPT.04.governance: Adopt ArcNotes: Family governance and policy tests (opens 1 task)
- ADOPT.04.release: Adopt ArcNotes: Release readiness and family release (opens 1 task)
- ADOPT.04.runtime-proofs: Adopt ArcNotes: Runtime proofs (opens 1 task)

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] ADOPT.01: frozen baseline record
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] ADOPT.04.app-composition: slice recorded
- [integration] ADOPT.04.arcnotes: slice recorded
- [integration] ADOPT.04.governance: slice recorded
- [integration] ADOPT.04.release: slice recorded
- [integration] ADOPT.04.runtime-proofs: slice recorded

Permitted write scope: Plan:ledger/adoption/ArcNotes.md; Plan:ledger/tasks/adopt-04.md

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Review of merged source, retained CI results and receipts only; no new builds, downloads or runtime checks (P2-017).
Completion evidence for the ledger: Repository adoption record with the repository-wide facts, links to every slice record, the combined classification table and any conflicts raised under D-001.
```

```text
Execute ArcForges delivery task ADOPT.05 — Adopt ArcScope.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/adopt-05 (python tools/delivery.py claim ADOPT.05 --worker <name>); task branch task/adopt-05 in Plan; ledger record ledger/tasks/adopt-05.md.
Kind/size: adoption/S. Baseline: not-started.
Outcome: The repository-wide adoption facts for ArcScope (main head, retained CI workflow inventory under P2-017, package identities and pins, shared roots and source inventory) are recorded once for its slices to cite, and the ArcScope classification table is complete when every adoption slice of the repository is complete.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- P2-018 (adoption stage: ArcScope repository record): C:\MyFile\Projects\ArcForges-Design-B\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-018

Adoption slices (claim, review and record each separately as ledger/tasks/<slice key>.md, for example ledger/tasks/adopt-05-arcscope.md, plus one ledger/tasks/<key>.md with status inherited per task it classifies as inherited; one pull request may carry several; each slice opens only its own repository lane; each has its own prompt under "Adoption slices" below):
- ADOPT.05.arcscope: Adopt ArcScope: ArcScope (opens 27 tasks)
- ADOPT.05.governance: Adopt ArcScope: Family governance and policy tests (opens 1 task)
- ADOPT.05.release: Adopt ArcScope: Release readiness and family release (opens 1 task)
- ADOPT.05.runtime-proofs: Adopt ArcScope: Runtime proofs (opens 1 task)
- ADOPT.05.simulator: Adopt ArcScope: ArcScope Cloud simulator (opens 1 task)

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] ADOPT.01: frozen baseline record
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] ADOPT.05.arcscope: slice recorded
- [integration] ADOPT.05.governance: slice recorded
- [integration] ADOPT.05.release: slice recorded
- [integration] ADOPT.05.runtime-proofs: slice recorded
- [integration] ADOPT.05.simulator: slice recorded

Permitted write scope: Plan:ledger/adoption/ArcScope.md; Plan:ledger/tasks/adopt-05.md

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Review of merged source, retained CI results and receipts only; no new builds, downloads or runtime checks (P2-017).
Completion evidence for the ledger: Repository adoption record with the repository-wide facts, links to every slice record, the combined classification table and any conflicts raised under D-001.
```

```text
Execute ArcForges delivery task ADOPT.06 — Adopt ArcSlate.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/adopt-06 (python tools/delivery.py claim ADOPT.06 --worker <name>); task branch task/adopt-06 in Plan; ledger record ledger/tasks/adopt-06.md.
Kind/size: adoption/S. Baseline: not-started.
Outcome: The repository-wide adoption facts for ArcSlate (main head, retained CI workflow inventory under P2-017, package identities and pins, shared roots and source inventory) are recorded once for its slices to cite, and the ArcSlate classification table is complete when every adoption slice of the repository is complete.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- P2-018 (adoption stage: ArcSlate repository record): C:\MyFile\Projects\ArcForges-Design-B\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-018

Adoption slices (claim, review and record each separately as ledger/tasks/<slice key>.md, for example ledger/tasks/adopt-06-arcslate.md, plus one ledger/tasks/<key>.md with status inherited per task it classifies as inherited; one pull request may carry several; each slice opens only its own repository lane; each has its own prompt under "Adoption slices" below):
- ADOPT.06.arcslate: Adopt ArcSlate: ArcSlate (opens 41 tasks)
- ADOPT.06.governance: Adopt ArcSlate: Family governance and policy tests (opens 1 task)
- ADOPT.06.release: Adopt ArcSlate: Release readiness and family release (opens 1 task)
- ADOPT.06.runtime-proofs: Adopt ArcSlate: Runtime proofs (opens 1 task)

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] ADOPT.01: frozen baseline record
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] ADOPT.06.arcslate: slice recorded
- [integration] ADOPT.06.governance: slice recorded
- [integration] ADOPT.06.release: slice recorded
- [integration] ADOPT.06.runtime-proofs: slice recorded

Permitted write scope: Plan:ledger/adoption/ArcSlate.md; Plan:ledger/tasks/adopt-06.md

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Review of merged source, retained CI results and receipts only; no new builds, downloads or runtime checks (P2-017).
Completion evidence for the ledger: Repository adoption record with the repository-wide facts, links to every slice record, the combined classification table and any conflicts raised under D-001.
```

```text
Execute ArcForges delivery task ADOPT.07 — Adopt Cloud.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/adopt-07 (python tools/delivery.py claim ADOPT.07 --worker <name>); task branch task/adopt-07 in Plan; ledger record ledger/tasks/adopt-07.md.
Kind/size: adoption/S. Baseline: not-started.
Outcome: The repository-wide adoption facts for Cloud (main head, retained CI workflow inventory under P2-017, package identities and pins, shared roots and source inventory) are recorded once for its slices to cite, and the Cloud classification table is complete when every adoption slice of the repository is complete.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- P2-018 (adoption stage: Cloud repository record): C:\MyFile\Projects\ArcForges-Design-B\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-018

Adoption slices (claim, review and record each separately as ledger/tasks/<slice key>.md, for example ledger/tasks/adopt-07-ai-routing.md, plus one ledger/tasks/<key>.md with status inherited per task it classifies as inherited; one pull request may carry several; each slice opens only its own repository lane; each has its own prompt under "Adoption slices" below):
- ADOPT.07.ai-routing: Adopt Cloud: Workers AI routing and metering (opens 6 tasks)
- ADOPT.07.cloud: Adopt Cloud: Cloud core (opens 58 tasks)
- ADOPT.07.commerce: Adopt Cloud: Commerce, entitlement and credits (opens 15 tasks)
- ADOPT.07.device-bridge: Adopt Cloud: Application presence and tool bridge (opens 9 tasks)
- ADOPT.07.extensions: Adopt Cloud: Extension platform and integrations (opens 1 task)
- ADOPT.07.governance: Adopt Cloud: Family governance and policy tests (opens 1 task)
- ADOPT.07.harness: Adopt Cloud: Cloud Harness (opens 2 tasks)
- ADOPT.07.operations: Adopt Cloud: Operations, support and trust and safety (opens 9 tasks)
- ADOPT.07.policy: Adopt Cloud: Dynamic policy and configuration (opens 10 tasks)
- ADOPT.07.release: Adopt Cloud: Release readiness and family release (opens 3 tasks)
- ADOPT.07.runtime-proofs: Adopt Cloud: Runtime proofs (opens 1 task)
- ADOPT.07.search: Adopt Cloud: Knowledge search and retrieval (opens 8 tasks)
- ADOPT.07.simulator: Adopt Cloud: ArcScope Cloud simulator (opens 9 tasks)

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] ADOPT.01: frozen baseline record
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] ADOPT.07.ai-routing: slice recorded
- [integration] ADOPT.07.cloud: slice recorded
- [integration] ADOPT.07.commerce: slice recorded
- [integration] ADOPT.07.device-bridge: slice recorded
- [integration] ADOPT.07.extensions: slice recorded
- [integration] ADOPT.07.governance: slice recorded
- [integration] ADOPT.07.harness: slice recorded
- [integration] ADOPT.07.operations: slice recorded
- [integration] ADOPT.07.policy: slice recorded
- [integration] ADOPT.07.release: slice recorded
- [integration] ADOPT.07.runtime-proofs: slice recorded
- [integration] ADOPT.07.search: slice recorded
- [integration] ADOPT.07.simulator: slice recorded

Permitted write scope: Plan:ledger/adoption/Cloud.md; Plan:ledger/tasks/adopt-07.md

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Review of merged source, retained CI results and receipts only; no new builds, downloads or runtime checks (P2-017).
Completion evidence for the ledger: Repository adoption record with the repository-wide facts, links to every slice record, the combined classification table and any conflicts raised under D-001.
```

```text
Execute ArcForges delivery task ADOPT.08 — Adopt AI.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/adopt-08 (python tools/delivery.py claim ADOPT.08 --worker <name>); task branch task/adopt-08 in Plan; ledger record ledger/tasks/adopt-08.md.
Kind/size: adoption/S. Baseline: not-started.
Outcome: The repository-wide adoption facts for AI (main head, retained CI workflow inventory under P2-017, package identities and pins, shared roots and source inventory) are recorded once for its slices to cite, and the AI classification table is complete when every adoption slice of the repository is complete.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- P2-018 (adoption stage: AI repository record): C:\MyFile\Projects\ArcForges-Design-B\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-018

Adoption slices (claim, review and record each separately as ledger/tasks/<slice key>.md, for example ledger/tasks/adopt-08-ai-routing.md, plus one ledger/tasks/<key>.md with status inherited per task it classifies as inherited; one pull request may carry several; each slice opens only its own repository lane; each has its own prompt under "Adoption slices" below):
- ADOPT.08.ai-routing: Adopt AI: Workers AI routing and metering (opens 5 tasks)
- ADOPT.08.extensions: Adopt AI: Extension platform and integrations (opens 1 task)
- ADOPT.08.governance: Adopt AI: Family governance and policy tests (opens 1 task)
- ADOPT.08.harness: Adopt AI: Cloud Harness (opens 7 tasks)

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] ADOPT.01: frozen baseline record
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] ADOPT.08.ai-routing: slice recorded
- [integration] ADOPT.08.extensions: slice recorded
- [integration] ADOPT.08.governance: slice recorded
- [integration] ADOPT.08.harness: slice recorded

Permitted write scope: Plan:ledger/adoption/AI.md; Plan:ledger/tasks/adopt-08.md

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Review of merged source, retained CI results and receipts only; no new builds, downloads or runtime checks (P2-017).
Completion evidence for the ledger: Repository adoption record with the repository-wide facts, links to every slice record, the combined classification table and any conflicts raised under D-001.
```

```text
Execute ArcForges delivery task ADOPT.09 — Adopt Web.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/adopt-09 (python tools/delivery.py claim ADOPT.09 --worker <name>); task branch task/adopt-09 in Plan; ledger record ledger/tasks/adopt-09.md.
Kind/size: adoption/S. Baseline: not-started.
Outcome: The repository-wide adoption facts for Web (main head, retained CI workflow inventory under P2-017, package identities and pins, shared roots and source inventory) are recorded once for its slices to cite, and the Web classification table is complete when every adoption slice of the repository is complete.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- P2-018 (adoption stage: Web repository record): C:\MyFile\Projects\ArcForges-Design-B\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-018

Adoption slices (claim, review and record each separately as ledger/tasks/<slice key>.md, for example ledger/tasks/adopt-09-governance.md, plus one ledger/tasks/<key>.md with status inherited per task it classifies as inherited; one pull request may carry several; each slice opens only its own repository lane; each has its own prompt under "Adoption slices" below):
- ADOPT.09.governance: Adopt Web: Family governance and policy tests (opens 1 task)
- ADOPT.09.operations: Adopt Web: Operations, support and trust and safety (opens 4 tasks)
- ADOPT.09.release: Adopt Web: Release readiness and family release (opens 1 task)
- ADOPT.09.runtime-proofs: Adopt Web: Runtime proofs (opens 1 task)
- ADOPT.09.web: Adopt Web: Web (opens 31 tasks)

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] ADOPT.01: frozen baseline record
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] ADOPT.09.governance: slice recorded
- [integration] ADOPT.09.operations: slice recorded
- [integration] ADOPT.09.release: slice recorded
- [integration] ADOPT.09.runtime-proofs: slice recorded
- [integration] ADOPT.09.web: slice recorded

Permitted write scope: Plan:ledger/adoption/Web.md; Plan:ledger/tasks/adopt-09.md

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Review of merged source, retained CI results and receipts only; no new builds, downloads or runtime checks (P2-017).
Completion evidence for the ledger: Repository adoption record with the repository-wide facts, links to every slice record, the combined classification table and any conflicts raised under D-001.
```

```text
Execute ArcForges delivery task ADOPT.10 — Adopt Mobile.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/adopt-10 (python tools/delivery.py claim ADOPT.10 --worker <name>); task branch task/adopt-10 in Plan; ledger record ledger/tasks/adopt-10.md.
Kind/size: adoption/S. Baseline: not-started.
Outcome: The repository-wide adoption facts for Mobile (main head, retained CI workflow inventory under P2-017, package identities and pins, shared roots and source inventory) are recorded once for its slices to cite, and the Mobile classification table is complete when every adoption slice of the repository is complete.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- P2-018 (adoption stage: Mobile repository record): C:\MyFile\Projects\ArcForges-Design-B\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-018

Adoption slices (claim, review and record each separately as ledger/tasks/<slice key>.md, for example ledger/tasks/adopt-10-android.md, plus one ledger/tasks/<key>.md with status inherited per task it classifies as inherited; one pull request may carry several; each slice opens only its own repository lane; each has its own prompt under "Adoption slices" below):
- ADOPT.10.android: Adopt Mobile: Android companion (opens 26 tasks)
- ADOPT.10.governance: Adopt Mobile: Family governance and policy tests (opens 1 task)
- ADOPT.10.release: Adopt Mobile: Release readiness and family release (opens 1 task)
- ADOPT.10.runtime-proofs: Adopt Mobile: Runtime proofs (opens 1 task)

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] ADOPT.01: frozen baseline record
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] ADOPT.10.android: slice recorded
- [integration] ADOPT.10.governance: slice recorded
- [integration] ADOPT.10.release: slice recorded
- [integration] ADOPT.10.runtime-proofs: slice recorded

Permitted write scope: Plan:ledger/adoption/Mobile.md; Plan:ledger/tasks/adopt-10.md

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Review of merged source, retained CI results and receipts only; no new builds, downloads or runtime checks (P2-017).
Completion evidence for the ledger: Repository adoption record with the repository-wide facts, links to every slice record, the combined classification table and any conflicts raised under D-001.
```

```text
Execute ArcForges delivery task ADOPT.11 — Reconcile Design and Plan documentation for adoption.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges-Design-B (integration owner: Design integration owner, the holder of roles/integration-design). Also touches: Plan.
Claim and handoff record: claims/adopt-11 (python tools/delivery.py claim ADOPT.11 --worker <name>); task branch task/adopt-11 in Design; ledger record ledger/tasks/adopt-11.md.
Kind/size: adoption/S. Baseline: not-started.
Outcome: Documentation findings that affect adoption decisions are resolved or scheduled (including the pre-existing corpus citation drift recorded in the adoption stage document), the generated views are confirmed current, and the ledger shows which adoption slices are complete.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- P2-018 (adoption stage: documentation reconciliation): C:\MyFile\Projects\ArcForges-Design-B\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-018

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] ADOPT.01: frozen baseline record
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Design:docs/**; Plan:ledger/adoption/documentation.md

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Documentation consistency and link review, delivery graph check and the existing corpus integrity check; no product builds (P2-017).
Completion evidence for the ledger: Reconciliation record with checker results and any planning-change pull requests.
```

## Adoption slices

Each slice is claimed, executed, reviewed and recorded on its own; several may share one pull request.

```text
Execute ArcForges adoption slice ADOPT.02.app-composition — Adopt DesktopPlatform: Application composition.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-02-app-composition); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\DesktopPlatform (lane app-composition); repository adoption task ADOPT.02 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-02-app-composition (python tools/delivery.py claim ADOPT.02.app-composition --worker <name>); task branch task/adopt-02-app-composition in Plan; ledger record ledger/tasks/adopt-02-app-composition.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- APP.01, APP.04, APP.05, APP.06, APP.07, APP.08
Opens when the record is merged: APP.01, APP.04, APP.05, APP.06, APP.07, APP.08, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-02-app-composition.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.02.assistant — Adopt DesktopPlatform: Embedded assistant.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-02-assistant); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\DesktopPlatform (lane assistant); repository adoption task ADOPT.02 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-02-assistant (python tools/delivery.py claim ADOPT.02.assistant --worker <name>); task branch task/adopt-02-assistant in Plan; ledger record ledger/tasks/adopt-02-assistant.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- AST.01, AST.02, AST.03, AST.04, AST.05, AST.06, AST.07, AST.08, AST.09, AST.10, AST.11, AST.12, AST.13, AST.14, AST.15, AST.16, AST.17, AST.18, AST.19, AST.20, AST.21, AST.22
Opens when the record is merged: AST.01, AST.02, AST.03, AST.04, AST.05, AST.06, AST.07, AST.08, AST.09, AST.10, AST.11, AST.12, AST.13, AST.14, AST.15, AST.16, AST.17, AST.18, AST.19, AST.20, AST.21, AST.22, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-02-assistant.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.02.cloud — Adopt DesktopPlatform: Cloud core.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-02-cloud); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\DesktopPlatform (lane cloud); repository adoption task ADOPT.02 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-02-cloud (python tools/delivery.py claim ADOPT.02.cloud --worker <name>); task branch task/adopt-02-cloud in Plan; ledger record ledger/tasks/adopt-02-cloud.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- CLOUD.18, CLOUD.38
Opens when the record is merged: CLOUD.18, CLOUD.38, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-02-cloud.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.02.device-bridge — Adopt DesktopPlatform: Application presence and tool bridge.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-02-device-bridge); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\DesktopPlatform (lane device-bridge); repository adoption task ADOPT.02 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-02-device-bridge (python tools/delivery.py claim ADOPT.02.device-bridge --worker <name>); task branch task/adopt-02-device-bridge in Plan; ledger record ledger/tasks/adopt-02-device-bridge.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- DEV.03, DEV.05, DEV.14
Opens when the record is merged: DEV.03, DEV.05, DEV.14, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-02-device-bridge.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.02.execution — Adopt DesktopPlatform: Execution engine.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-02-execution); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\DesktopPlatform (lane execution); repository adoption task ADOPT.02 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-02-execution (python tools/delivery.py claim ADOPT.02.execution --worker <name>); task branch task/adopt-02-execution in Plan; ledger record ledger/tasks/adopt-02-execution.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- EXE.01, EXE.02, EXE.03, EXE.04, EXE.05, EXE.06, EXE.07, EXE.08, EXE.09
Opens when the record is merged: EXE.01, EXE.02, EXE.03, EXE.04, EXE.05, EXE.06, EXE.07, EXE.08, EXE.09, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-02-execution.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.02.extensions — Adopt DesktopPlatform: Extension platform and integrations.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-02-extensions); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\DesktopPlatform (lane extensions); repository adoption task ADOPT.02 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-02-extensions (python tools/delivery.py claim ADOPT.02.extensions --worker <name>); task branch task/adopt-02-extensions in Plan; ledger record ledger/tasks/adopt-02-extensions.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- EXT.00, EXT.01, EXT.03, EXT.05, EXT.07, EXT.09, EXT.90
Opens when the record is merged: EXT.00, EXT.01, EXT.03, EXT.05, EXT.07, EXT.09, EXT.90, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-02-extensions.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.02.foundation — Adopt DesktopPlatform: Foundation values.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-02-foundation); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\DesktopPlatform (lane foundation); repository adoption task ADOPT.02 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-02-foundation (python tools/delivery.py claim ADOPT.02.foundation --worker <name>); task branch task/adopt-02-foundation in Plan; ledger record ledger/tasks/adopt-02-foundation.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- FND.01, FND.02, FND.03, FND.04, FND.05, FND.06, FND.07
Opens when the record is merged: FND.01, FND.02, FND.03, FND.04, FND.05, FND.06, FND.07, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-02-foundation.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.02.governance — Adopt DesktopPlatform: Family governance and policy tests.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-02-governance); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\DesktopPlatform (lane governance); repository adoption task ADOPT.02 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-02-governance (python tools/delivery.py claim ADOPT.02.governance --worker <name>); task branch task/adopt-02-governance in Plan; ledger record ledger/tasks/adopt-02-governance.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- GOV.01, GOV.02, GOV.03, GOV.04, GOV.13, GOV.14, GOV.15
Opens when the record is merged: GOV.04, GOV.13, GOV.14, GOV.15, except any task this slice classifies as inherited. Every task classified as inherited, including the accepted-baseline tasks GOV.01, GOV.02, GOV.03, gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-02-governance.md; Plan:ledger/tasks/gov-01.md; Plan:ledger/tasks/gov-02.md; Plan:ledger/tasks/gov-03.md; Plan:ledger/tasks/<key>.md (status inherited) for each other task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.02.native — Adopt DesktopPlatform: Native producers and probes.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-02-native); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\DesktopPlatform (lane native); repository adoption task ADOPT.02 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-02-native (python tools/delivery.py claim ADOPT.02.native --worker <name>); task branch task/adopt-02-native in Plan; ledger record ledger/tasks/adopt-02-native.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- NAT.01, NAT.02, NAT.03, NAT.04, NAT.05, NAT.06, NAT.07, NAT.08, NAT.09, NAT.10, NAT.11, NAT.12, NAT.13, NAT.14, NAT.15, NAT.20, NAT.21, NAT.22, NAT.23, NAT.24, NAT.25, NAT.26, NAT.28, NAT.29, NAT.30
Opens when the record is merged: NAT.01, NAT.02, NAT.03, NAT.04, NAT.05, NAT.06, NAT.07, NAT.08, NAT.09, NAT.10, NAT.11, NAT.12, NAT.13, NAT.14, NAT.15, NAT.20, NAT.21, NAT.22, NAT.23, NAT.24, NAT.25, NAT.26, NAT.28, NAT.29, NAT.30, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-02-native.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.02.platform — Adopt DesktopPlatform: Desktop platform mechanisms.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-02-platform); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\DesktopPlatform (lane platform); repository adoption task ADOPT.02 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-02-platform (python tools/delivery.py claim ADOPT.02.platform --worker <name>); task branch task/adopt-02-platform in Plan; ledger record ledger/tasks/adopt-02-platform.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- PLT.01, PLT.02, PLT.03, PLT.04, PLT.05, PLT.06, PLT.07, PLT.08, PLT.09, PLT.10, PLT.11, PLT.12, PLT.13, PLT.14, PLT.15, PLT.16, PLT.17, PLT.18, PLT.19, PLT.20, PLT.21, PLT.22, PLT.23, PLT.24, PLT.25, PLT.26, PLT.27, PLT.28, PLT.29, PLT.30, PLT.31, PLT.32, PLT.33, PLT.34, PLT.35, PLT.36, PLT.37, PLT.38, PLT.39, PLT.40, PLT.41, PLT.42, PLT.43, PLT.44, PLT.45, PLT.46, PLT.47, PLT.48, PLT.49, PLT.50, PLT.51, PLT.52, PLT.53, PLT.54, PLT.56, PLT.57
Opens when the record is merged: PLT.01, PLT.02, PLT.03, PLT.04, PLT.05, PLT.06, PLT.07, PLT.08, PLT.09, PLT.10, PLT.11, PLT.12, PLT.13, PLT.14, PLT.15, PLT.16, PLT.17, PLT.18, PLT.19, PLT.20, PLT.21, PLT.22, PLT.23, PLT.24, PLT.25, PLT.26, PLT.27, PLT.28, PLT.29, PLT.30, PLT.31, PLT.32, PLT.33, PLT.34, PLT.35, PLT.36, PLT.37, PLT.38, PLT.39, PLT.40, PLT.41, PLT.42, PLT.43, PLT.44, PLT.45, PLT.46, PLT.47, PLT.48, PLT.49, PLT.50, PLT.51, PLT.52, PLT.53, PLT.54, PLT.56, PLT.57, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-02-platform.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.02.policy — Adopt DesktopPlatform: Dynamic policy and configuration.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-02-policy); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\DesktopPlatform (lane policy); repository adoption task ADOPT.02 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-02-policy (python tools/delivery.py claim ADOPT.02.policy --worker <name>); task branch task/adopt-02-policy in Plan; ledger record ledger/tasks/adopt-02-policy.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- POL.09
Opens when the record is merged: POL.09, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-02-policy.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.02.release — Adopt DesktopPlatform: Release readiness and family release.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-02-release); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\DesktopPlatform (lane release); repository adoption task ADOPT.02 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-02-release (python tools/delivery.py claim ADOPT.02.release --worker <name>); task branch task/adopt-02-release in Plan; ledger record ledger/tasks/adopt-02-release.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- REL.10, REL.11
Opens when the record is merged: REL.10, REL.11, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-02-release.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.02.runtime-proofs — Adopt DesktopPlatform: Runtime proofs.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-02-runtime-proofs); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\DesktopPlatform (lane runtime-proofs); repository adoption task ADOPT.02 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-02-runtime-proofs (python tools/delivery.py claim ADOPT.02.runtime-proofs --worker <name>); task branch task/adopt-02-runtime-proofs in Plan; ledger record ledger/tasks/adopt-02-runtime-proofs.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- PRF.04, PRF.05, PRF.06, PRF.09
Opens when the record is merged: PRF.04, PRF.05, PRF.06, PRF.09, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-02-runtime-proofs.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.02.updater — Adopt DesktopPlatform: Desktop distribution and update.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-02-updater); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\DesktopPlatform (lane updater); repository adoption task ADOPT.02 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-02-updater (python tools/delivery.py claim ADOPT.02.updater --worker <name>); task branch task/adopt-02-updater in Plan; ledger record ledger/tasks/adopt-02-updater.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- UPD.01, UPD.02, UPD.03, UPD.04, UPD.05, UPD.06, UPD.07, UPD.08
Opens when the record is merged: UPD.01, UPD.02, UPD.03, UPD.04, UPD.05, UPD.06, UPD.07, UPD.08, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-02-updater.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.03.contracts — Adopt Contracts: Contracts schema closures.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-03-contracts); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Contracts (lane contracts); repository adoption task ADOPT.03 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-03-contracts (python tools/delivery.py claim ADOPT.03.contracts --worker <name>); task branch task/adopt-03-contracts in Plan; ledger record ledger/tasks/adopt-03-contracts.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- CON.01, CON.02, CON.03, CON.04, CON.05, CON.06, CON.07, CON.08, CON.09, CON.10, CON.11, CON.12, CON.13, CON.14, CON.15, CON.16, CON.17, CON.18, CON.19, CON.20, CON.21, CON.22, CON.90, CON.91, CON.92
Opens when the record is merged: CON.01, CON.02, CON.03, CON.04, CON.05, CON.06, CON.07, CON.08, CON.09, CON.10, CON.11, CON.12, CON.13, CON.14, CON.15, CON.16, CON.17, CON.18, CON.19, CON.20, CON.21, CON.22, except any task this slice classifies as inherited. Every task classified as inherited, including the accepted-baseline tasks CON.90, CON.91, CON.92, gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-03-contracts.md; Plan:ledger/tasks/con-90.md; Plan:ledger/tasks/con-91.md; Plan:ledger/tasks/con-92.md; Plan:ledger/tasks/<key>.md (status inherited) for each other task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.03.extensions — Adopt Contracts: Extension platform and integrations.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-03-extensions); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Contracts (lane extensions); repository adoption task ADOPT.03 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-03-extensions (python tools/delivery.py claim ADOPT.03.extensions --worker <name>); task branch task/adopt-03-extensions in Plan; ledger record ledger/tasks/adopt-03-extensions.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- EXT.02, EXT.04, EXT.08
Opens when the record is merged: EXT.02, EXT.04, EXT.08, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-03-extensions.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.03.governance — Adopt Contracts: Family governance and policy tests.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-03-governance); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Contracts (lane governance); repository adoption task ADOPT.03 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-03-governance (python tools/delivery.py claim ADOPT.03.governance --worker <name>); task branch task/adopt-03-governance in Plan; ledger record ledger/tasks/adopt-03-governance.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- GOV.05, GOV.16
Opens when the record is merged: GOV.05, GOV.16, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-03-governance.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.03.release — Adopt Contracts: Release readiness and family release.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-03-release); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Contracts (lane release); repository adoption task ADOPT.03 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-03-release (python tools/delivery.py claim ADOPT.03.release --worker <name>); task branch task/adopt-03-release in Plan; ledger record ledger/tasks/adopt-03-release.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- REL.07
Opens when the record is merged: REL.07, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-03-release.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.04.app-composition — Adopt ArcNotes: Application composition.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-04-app-composition); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\ArcNotes (lane app-composition); repository adoption task ADOPT.04 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-04-app-composition (python tools/delivery.py claim ADOPT.04.app-composition --worker <name>); task branch task/adopt-04-app-composition in Plan; ledger record ledger/tasks/adopt-04-app-composition.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- APP.02, APP.03
Opens when the record is merged: APP.02, APP.03, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-04-app-composition.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.04.arcnotes — Adopt ArcNotes: ArcNotes.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-04-arcnotes); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\ArcNotes (lane arcnotes); repository adoption task ADOPT.04 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-04-arcnotes (python tools/delivery.py claim ADOPT.04.arcnotes --worker <name>); task branch task/adopt-04-arcnotes in Plan; ledger record ledger/tasks/adopt-04-arcnotes.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- NOTES.01, NOTES.02, NOTES.03, NOTES.04, NOTES.05, NOTES.06, NOTES.07, NOTES.08, NOTES.09, NOTES.10, NOTES.11, NOTES.12, NOTES.13, NOTES.14, NOTES.15, NOTES.16, NOTES.17, NOTES.18, NOTES.19, NOTES.20, NOTES.21, NOTES.22, NOTES.23, NOTES.24, NOTES.26, NOTES.27, NOTES.28, NOTES.29, NOTES.30, NOTES.31, NOTES.32, NOTES.33, NOTES.34, NOTES.35, NOTES.37
Opens when the record is merged: NOTES.01, NOTES.02, NOTES.03, NOTES.04, NOTES.05, NOTES.06, NOTES.07, NOTES.08, NOTES.09, NOTES.10, NOTES.11, NOTES.12, NOTES.13, NOTES.14, NOTES.15, NOTES.16, NOTES.17, NOTES.18, NOTES.19, NOTES.20, NOTES.21, NOTES.22, NOTES.23, NOTES.24, NOTES.26, NOTES.27, NOTES.28, NOTES.29, NOTES.30, NOTES.31, NOTES.32, NOTES.33, NOTES.34, NOTES.35, NOTES.37, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-04-arcnotes.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.04.governance — Adopt ArcNotes: Family governance and policy tests.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-04-governance); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\ArcNotes (lane governance); repository adoption task ADOPT.04 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-04-governance (python tools/delivery.py claim ADOPT.04.governance --worker <name>); task branch task/adopt-04-governance in Plan; ledger record ledger/tasks/adopt-04-governance.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- GOV.06
Opens when the record is merged: GOV.06, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-04-governance.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.04.release — Adopt ArcNotes: Release readiness and family release.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-04-release); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\ArcNotes (lane release); repository adoption task ADOPT.04 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-04-release (python tools/delivery.py claim ADOPT.04.release --worker <name>); task branch task/adopt-04-release in Plan; ledger record ledger/tasks/adopt-04-release.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- REL.01
Opens when the record is merged: REL.01, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-04-release.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.04.runtime-proofs — Adopt ArcNotes: Runtime proofs.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-04-runtime-proofs); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\ArcNotes (lane runtime-proofs); repository adoption task ADOPT.04 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-04-runtime-proofs (python tools/delivery.py claim ADOPT.04.runtime-proofs --worker <name>); task branch task/adopt-04-runtime-proofs in Plan; ledger record ledger/tasks/adopt-04-runtime-proofs.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- PRF.01
Opens when the record is merged: PRF.01, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-04-runtime-proofs.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.05.arcscope — Adopt ArcScope: ArcScope.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-05-arcscope); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\ArcScope (lane arcscope); repository adoption task ADOPT.05 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-05-arcscope (python tools/delivery.py claim ADOPT.05.arcscope --worker <name>); task branch task/adopt-05-arcscope in Plan; ledger record ledger/tasks/adopt-05-arcscope.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- SCOPE.01, SCOPE.02, SCOPE.03, SCOPE.04, SCOPE.05, SCOPE.06, SCOPE.07, SCOPE.08, SCOPE.09, SCOPE.10, SCOPE.11, SCOPE.12, SCOPE.13, SCOPE.14, SCOPE.15, SCOPE.16, SCOPE.17, SCOPE.18, SCOPE.19, SCOPE.20, SCOPE.21, SCOPE.22, SCOPE.23, SCOPE.24, SCOPE.25, SCOPE.26, SCOPE.27
Opens when the record is merged: SCOPE.01, SCOPE.02, SCOPE.03, SCOPE.04, SCOPE.05, SCOPE.06, SCOPE.07, SCOPE.08, SCOPE.09, SCOPE.10, SCOPE.11, SCOPE.12, SCOPE.13, SCOPE.14, SCOPE.15, SCOPE.16, SCOPE.17, SCOPE.18, SCOPE.19, SCOPE.20, SCOPE.21, SCOPE.22, SCOPE.23, SCOPE.24, SCOPE.25, SCOPE.26, SCOPE.27, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-05-arcscope.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.05.governance — Adopt ArcScope: Family governance and policy tests.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-05-governance); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\ArcScope (lane governance); repository adoption task ADOPT.05 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-05-governance (python tools/delivery.py claim ADOPT.05.governance --worker <name>); task branch task/adopt-05-governance in Plan; ledger record ledger/tasks/adopt-05-governance.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- GOV.07
Opens when the record is merged: GOV.07, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-05-governance.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.05.release — Adopt ArcScope: Release readiness and family release.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-05-release); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\ArcScope (lane release); repository adoption task ADOPT.05 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-05-release (python tools/delivery.py claim ADOPT.05.release --worker <name>); task branch task/adopt-05-release in Plan; ledger record ledger/tasks/adopt-05-release.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- REL.02
Opens when the record is merged: REL.02, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-05-release.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.05.runtime-proofs — Adopt ArcScope: Runtime proofs.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-05-runtime-proofs); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\ArcScope (lane runtime-proofs); repository adoption task ADOPT.05 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-05-runtime-proofs (python tools/delivery.py claim ADOPT.05.runtime-proofs --worker <name>); task branch task/adopt-05-runtime-proofs in Plan; ledger record ledger/tasks/adopt-05-runtime-proofs.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- PRF.02
Opens when the record is merged: PRF.02, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-05-runtime-proofs.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.05.simulator — Adopt ArcScope: ArcScope Cloud simulator.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-05-simulator); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\ArcScope (lane simulator); repository adoption task ADOPT.05 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-05-simulator (python tools/delivery.py claim ADOPT.05.simulator --worker <name>); task branch task/adopt-05-simulator in Plan; ledger record ledger/tasks/adopt-05-simulator.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- SIM.06
Opens when the record is merged: SIM.06, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-05-simulator.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.06.arcslate — Adopt ArcSlate: ArcSlate.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-06-arcslate); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\ArcSlate (lane arcslate); repository adoption task ADOPT.06 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-06-arcslate (python tools/delivery.py claim ADOPT.06.arcslate --worker <name>); task branch task/adopt-06-arcslate in Plan; ledger record ledger/tasks/adopt-06-arcslate.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- SLATE.01, SLATE.02, SLATE.03, SLATE.04, SLATE.05, SLATE.06, SLATE.07, SLATE.08, SLATE.09, SLATE.10, SLATE.11, SLATE.12, SLATE.13, SLATE.14, SLATE.15, SLATE.16, SLATE.17, SLATE.18, SLATE.19, SLATE.20, SLATE.21, SLATE.22, SLATE.23, SLATE.24, SLATE.25, SLATE.26, SLATE.27, SLATE.28, SLATE.29, SLATE.30, SLATE.31, SLATE.32, SLATE.33, SLATE.34, SLATE.35, SLATE.36, SLATE.37, SLATE.38, SLATE.39, SLATE.40, SLATE.42
Opens when the record is merged: SLATE.01, SLATE.02, SLATE.03, SLATE.04, SLATE.05, SLATE.06, SLATE.07, SLATE.08, SLATE.09, SLATE.10, SLATE.11, SLATE.12, SLATE.13, SLATE.14, SLATE.15, SLATE.16, SLATE.17, SLATE.18, SLATE.19, SLATE.20, SLATE.21, SLATE.22, SLATE.23, SLATE.24, SLATE.25, SLATE.26, SLATE.27, SLATE.28, SLATE.29, SLATE.30, SLATE.31, SLATE.32, SLATE.33, SLATE.34, SLATE.35, SLATE.36, SLATE.37, SLATE.38, SLATE.39, SLATE.40, SLATE.42, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-06-arcslate.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.06.governance — Adopt ArcSlate: Family governance and policy tests.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-06-governance); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\ArcSlate (lane governance); repository adoption task ADOPT.06 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-06-governance (python tools/delivery.py claim ADOPT.06.governance --worker <name>); task branch task/adopt-06-governance in Plan; ledger record ledger/tasks/adopt-06-governance.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- GOV.08
Opens when the record is merged: GOV.08, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-06-governance.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.06.release — Adopt ArcSlate: Release readiness and family release.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-06-release); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\ArcSlate (lane release); repository adoption task ADOPT.06 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-06-release (python tools/delivery.py claim ADOPT.06.release --worker <name>); task branch task/adopt-06-release in Plan; ledger record ledger/tasks/adopt-06-release.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- REL.03
Opens when the record is merged: REL.03, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-06-release.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.06.runtime-proofs — Adopt ArcSlate: Runtime proofs.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-06-runtime-proofs); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\ArcSlate (lane runtime-proofs); repository adoption task ADOPT.06 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-06-runtime-proofs (python tools/delivery.py claim ADOPT.06.runtime-proofs --worker <name>); task branch task/adopt-06-runtime-proofs in Plan; ledger record ledger/tasks/adopt-06-runtime-proofs.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- PRF.03
Opens when the record is merged: PRF.03, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-06-runtime-proofs.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.07.ai-routing — Adopt Cloud: Workers AI routing and metering.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-07-ai-routing); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Cloud (lane ai-routing); repository adoption task ADOPT.07 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-07-ai-routing (python tools/delivery.py claim ADOPT.07.ai-routing --worker <name>); task branch task/adopt-07-ai-routing in Plan; ledger record ledger/tasks/adopt-07-ai-routing.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- AIR.01, AIR.02, AIR.03, AIR.04, AIR.06, AIR.90
Opens when the record is merged: AIR.01, AIR.02, AIR.03, AIR.04, AIR.06, AIR.90, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-07-ai-routing.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.07.cloud — Adopt Cloud: Cloud core.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-07-cloud); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Cloud (lane cloud); repository adoption task ADOPT.07 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-07-cloud (python tools/delivery.py claim ADOPT.07.cloud --worker <name>); task branch task/adopt-07-cloud in Plan; ledger record ledger/tasks/adopt-07-cloud.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- CLOUD.01, CLOUD.02, CLOUD.03, CLOUD.04, CLOUD.05, CLOUD.06, CLOUD.07, CLOUD.08, CLOUD.09, CLOUD.10, CLOUD.11, CLOUD.12, CLOUD.13, CLOUD.14, CLOUD.15, CLOUD.16, CLOUD.17, CLOUD.19, CLOUD.20, CLOUD.21, CLOUD.22, CLOUD.23, CLOUD.24, CLOUD.25, CLOUD.26, CLOUD.27, CLOUD.28, CLOUD.29, CLOUD.30, CLOUD.31, CLOUD.32, CLOUD.33, CLOUD.34, CLOUD.35, CLOUD.36, CLOUD.37, CLOUD.39, CLOUD.40, CLOUD.41, CLOUD.42, CLOUD.43, CLOUD.44, CLOUD.45, CLOUD.46, CLOUD.47, CLOUD.48, CLOUD.49, CLOUD.50, CLOUD.51, CLOUD.52, CLOUD.53, CLOUD.54, CLOUD.55, CLOUD.58, CLOUD.63, CLOUD.64, CLOUD.66, CLOUD.67
Opens when the record is merged: CLOUD.01, CLOUD.02, CLOUD.03, CLOUD.04, CLOUD.05, CLOUD.06, CLOUD.07, CLOUD.08, CLOUD.09, CLOUD.10, CLOUD.11, CLOUD.12, CLOUD.13, CLOUD.14, CLOUD.15, CLOUD.16, CLOUD.17, CLOUD.19, CLOUD.20, CLOUD.21, CLOUD.22, CLOUD.23, CLOUD.24, CLOUD.25, CLOUD.26, CLOUD.27, CLOUD.28, CLOUD.29, CLOUD.30, CLOUD.31, CLOUD.32, CLOUD.33, CLOUD.34, CLOUD.35, CLOUD.36, CLOUD.37, CLOUD.39, CLOUD.40, CLOUD.41, CLOUD.42, CLOUD.43, CLOUD.44, CLOUD.45, CLOUD.46, CLOUD.47, CLOUD.48, CLOUD.49, CLOUD.50, CLOUD.51, CLOUD.52, CLOUD.53, CLOUD.54, CLOUD.55, CLOUD.58, CLOUD.63, CLOUD.64, CLOUD.66, CLOUD.67, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-07-cloud.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.07.commerce — Adopt Cloud: Commerce, entitlement and credits.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-07-commerce); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Cloud (lane commerce); repository adoption task ADOPT.07 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-07-commerce (python tools/delivery.py claim ADOPT.07.commerce --worker <name>); task branch task/adopt-07-commerce in Plan; ledger record ledger/tasks/adopt-07-commerce.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- COM.01, COM.02, COM.03, COM.04, COM.05, COM.06, COM.07, COM.08, COM.09, COM.10, COM.11, COM.12, COM.13, COM.14, COM.15
Opens when the record is merged: COM.01, COM.02, COM.03, COM.04, COM.05, COM.06, COM.07, COM.08, COM.09, COM.10, COM.11, COM.12, COM.13, COM.14, COM.15, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-07-commerce.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.07.device-bridge — Adopt Cloud: Application presence and tool bridge.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-07-device-bridge); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Cloud (lane device-bridge); repository adoption task ADOPT.07 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-07-device-bridge (python tools/delivery.py claim ADOPT.07.device-bridge --worker <name>); task branch task/adopt-07-device-bridge in Plan; ledger record ledger/tasks/adopt-07-device-bridge.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- DEV.01, DEV.02, DEV.04, DEV.06, DEV.07, DEV.08, DEV.09, DEV.12, DEV.13
Opens when the record is merged: DEV.01, DEV.02, DEV.04, DEV.06, DEV.07, DEV.08, DEV.09, DEV.12, DEV.13, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-07-device-bridge.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.07.extensions — Adopt Cloud: Extension platform and integrations.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-07-extensions); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Cloud (lane extensions); repository adoption task ADOPT.07 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-07-extensions (python tools/delivery.py claim ADOPT.07.extensions --worker <name>); task branch task/adopt-07-extensions in Plan; ledger record ledger/tasks/adopt-07-extensions.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- EXT.06
Opens when the record is merged: EXT.06, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-07-extensions.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.07.governance — Adopt Cloud: Family governance and policy tests.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-07-governance); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Cloud (lane governance); repository adoption task ADOPT.07 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-07-governance (python tools/delivery.py claim ADOPT.07.governance --worker <name>); task branch task/adopt-07-governance in Plan; ledger record ledger/tasks/adopt-07-governance.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- GOV.09
Opens when the record is merged: GOV.09, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-07-governance.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.07.harness — Adopt Cloud: Cloud Harness.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-07-harness); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Cloud (lane harness); repository adoption task ADOPT.07 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-07-harness (python tools/delivery.py claim ADOPT.07.harness --worker <name>); task branch task/adopt-07-harness in Plan; ledger record ledger/tasks/adopt-07-harness.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- HAR.04, HAR.06
Opens when the record is merged: HAR.04, HAR.06, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-07-harness.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.07.operations — Adopt Cloud: Operations, support and trust and safety.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-07-operations); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Cloud (lane operations); repository adoption task ADOPT.07 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-07-operations (python tools/delivery.py claim ADOPT.07.operations --worker <name>); task branch task/adopt-07-operations in Plan; ledger record ledger/tasks/adopt-07-operations.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- OPS.01, OPS.02, OPS.03, OPS.06, OPS.07, OPS.08, OPS.09, OPS.10, OPS.12
Opens when the record is merged: OPS.01, OPS.02, OPS.03, OPS.06, OPS.07, OPS.08, OPS.09, OPS.10, OPS.12, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-07-operations.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.07.policy — Adopt Cloud: Dynamic policy and configuration.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-07-policy); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Cloud (lane policy); repository adoption task ADOPT.07 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-07-policy (python tools/delivery.py claim ADOPT.07.policy --worker <name>); task branch task/adopt-07-policy in Plan; ledger record ledger/tasks/adopt-07-policy.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- POL.01, POL.02, POL.03, POL.04, POL.05, POL.06, POL.07, POL.08, POL.10, POL.11
Opens when the record is merged: POL.01, POL.02, POL.03, POL.04, POL.05, POL.06, POL.07, POL.08, POL.10, POL.11, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-07-policy.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.07.release — Adopt Cloud: Release readiness and family release.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-07-release); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Cloud (lane release); repository adoption task ADOPT.07 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-07-release (python tools/delivery.py claim ADOPT.07.release --worker <name>); task branch task/adopt-07-release in Plan; ledger record ledger/tasks/adopt-07-release.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- REL.06, REL.08, REL.09
Opens when the record is merged: REL.06, REL.08, REL.09, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-07-release.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.07.runtime-proofs — Adopt Cloud: Runtime proofs.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-07-runtime-proofs); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Cloud (lane runtime-proofs); repository adoption task ADOPT.07 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-07-runtime-proofs (python tools/delivery.py claim ADOPT.07.runtime-proofs --worker <name>); task branch task/adopt-07-runtime-proofs in Plan; ledger record ledger/tasks/adopt-07-runtime-proofs.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- PRF.07
Opens when the record is merged: PRF.07, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-07-runtime-proofs.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.07.search — Adopt Cloud: Knowledge search and retrieval.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-07-search); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Cloud (lane search); repository adoption task ADOPT.07 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-07-search (python tools/delivery.py claim ADOPT.07.search --worker <name>); task branch task/adopt-07-search in Plan; ledger record ledger/tasks/adopt-07-search.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- SRCH.00, SRCH.01, SRCH.02, SRCH.03, SRCH.04, SRCH.05, SRCH.06, SRCH.90
Opens when the record is merged: SRCH.00, SRCH.01, SRCH.02, SRCH.03, SRCH.04, SRCH.05, SRCH.06, SRCH.90, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-07-search.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.07.simulator — Adopt Cloud: ArcScope Cloud simulator.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-07-simulator); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Cloud (lane simulator); repository adoption task ADOPT.07 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-07-simulator (python tools/delivery.py claim ADOPT.07.simulator --worker <name>); task branch task/adopt-07-simulator in Plan; ledger record ledger/tasks/adopt-07-simulator.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- SIM.01, SIM.02, SIM.03, SIM.04, SIM.05, SIM.07, SIM.08, SIM.09, SIM.10
Opens when the record is merged: SIM.01, SIM.02, SIM.03, SIM.04, SIM.05, SIM.07, SIM.08, SIM.09, SIM.10, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-07-simulator.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.08.ai-routing — Adopt AI: Workers AI routing and metering.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-08-ai-routing); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\AI (lane ai-routing); repository adoption task ADOPT.08 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-08-ai-routing (python tools/delivery.py claim ADOPT.08.ai-routing --worker <name>); task branch task/adopt-08-ai-routing in Plan; ledger record ledger/tasks/adopt-08-ai-routing.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- AIR.00, AIR.05, AIR.07, AIR.08, AIR.09
Opens when the record is merged: AIR.00, AIR.05, AIR.07, AIR.08, AIR.09, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-08-ai-routing.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.08.extensions — Adopt AI: Extension platform and integrations.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-08-extensions); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\AI (lane extensions); repository adoption task ADOPT.08 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-08-extensions (python tools/delivery.py claim ADOPT.08.extensions --worker <name>); task branch task/adopt-08-extensions in Plan; ledger record ledger/tasks/adopt-08-extensions.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- EXT.10
Opens when the record is merged: EXT.10, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-08-extensions.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.08.governance — Adopt AI: Family governance and policy tests.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-08-governance); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\AI (lane governance); repository adoption task ADOPT.08 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-08-governance (python tools/delivery.py claim ADOPT.08.governance --worker <name>); task branch task/adopt-08-governance in Plan; ledger record ledger/tasks/adopt-08-governance.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- GOV.10
Opens when the record is merged: GOV.10, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-08-governance.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.08.harness — Adopt AI: Cloud Harness.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-08-harness); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\AI (lane harness); repository adoption task ADOPT.08 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-08-harness (python tools/delivery.py claim ADOPT.08.harness --worker <name>); task branch task/adopt-08-harness in Plan; ledger record ledger/tasks/adopt-08-harness.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- HAR.00, HAR.01, HAR.02, HAR.03, HAR.05, HAR.90, HAR.91
Opens when the record is merged: HAR.00, HAR.01, HAR.02, HAR.03, HAR.05, HAR.90, HAR.91, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-08-harness.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.09.governance — Adopt Web: Family governance and policy tests.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-09-governance); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Web (lane governance); repository adoption task ADOPT.09 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-09-governance (python tools/delivery.py claim ADOPT.09.governance --worker <name>); task branch task/adopt-09-governance in Plan; ledger record ledger/tasks/adopt-09-governance.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- GOV.11
Opens when the record is merged: GOV.11, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-09-governance.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.09.operations — Adopt Web: Operations, support and trust and safety.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-09-operations); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Web (lane operations); repository adoption task ADOPT.09 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-09-operations (python tools/delivery.py claim ADOPT.09.operations --worker <name>); task branch task/adopt-09-operations in Plan; ledger record ledger/tasks/adopt-09-operations.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- OPS.04, OPS.05, OPS.11, OPS.13
Opens when the record is merged: OPS.04, OPS.05, OPS.11, OPS.13, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-09-operations.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.09.release — Adopt Web: Release readiness and family release.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-09-release); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Web (lane release); repository adoption task ADOPT.09 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-09-release (python tools/delivery.py claim ADOPT.09.release --worker <name>); task branch task/adopt-09-release in Plan; ledger record ledger/tasks/adopt-09-release.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- REL.05
Opens when the record is merged: REL.05, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-09-release.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.09.runtime-proofs — Adopt Web: Runtime proofs.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-09-runtime-proofs); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Web (lane runtime-proofs); repository adoption task ADOPT.09 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-09-runtime-proofs (python tools/delivery.py claim ADOPT.09.runtime-proofs --worker <name>); task branch task/adopt-09-runtime-proofs in Plan; ledger record ledger/tasks/adopt-09-runtime-proofs.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- PRF.08
Opens when the record is merged: PRF.08, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-09-runtime-proofs.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.09.web — Adopt Web: Web.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-09-web); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Web (lane web); repository adoption task ADOPT.09 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-09-web (python tools/delivery.py claim ADOPT.09.web --worker <name>); task branch task/adopt-09-web in Plan; ledger record ledger/tasks/adopt-09-web.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- WEB.01, WEB.02, WEB.03, WEB.04, WEB.05, WEB.06, WEB.07, WEB.08, WEB.09, WEB.10, WEB.11, WEB.12, WEB.13, WEB.14, WEB.15, WEB.16, WEB.17, WEB.18, WEB.19, WEB.20, WEB.21, WEB.22, WEB.23, WEB.24, WEB.25, WEB.26, WEB.27, WEB.28, WEB.29, WEB.30, WEB.31
Opens when the record is merged: WEB.01, WEB.02, WEB.03, WEB.04, WEB.05, WEB.06, WEB.07, WEB.08, WEB.09, WEB.10, WEB.11, WEB.12, WEB.13, WEB.14, WEB.15, WEB.16, WEB.17, WEB.18, WEB.19, WEB.20, WEB.21, WEB.22, WEB.23, WEB.24, WEB.25, WEB.26, WEB.27, WEB.28, WEB.29, WEB.30, WEB.31, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-09-web.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.10.android — Adopt Mobile: Android companion.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-10-android); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Mobile (lane android); repository adoption task ADOPT.10 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-10-android (python tools/delivery.py claim ADOPT.10.android --worker <name>); task branch task/adopt-10-android in Plan; ledger record ledger/tasks/adopt-10-android.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- AND.01, AND.02, AND.03, AND.04, AND.05, AND.06, AND.07, AND.08, AND.09, AND.10, AND.11, AND.12, AND.13, AND.14, AND.15, AND.16, AND.17, AND.18, AND.19, AND.20, AND.21, AND.22, AND.23, AND.24, AND.25, AND.26
Opens when the record is merged: AND.01, AND.02, AND.03, AND.04, AND.05, AND.06, AND.07, AND.08, AND.09, AND.10, AND.11, AND.12, AND.13, AND.14, AND.15, AND.16, AND.17, AND.18, AND.19, AND.20, AND.21, AND.22, AND.23, AND.24, AND.25, AND.26, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-10-android.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.10.governance — Adopt Mobile: Family governance and policy tests.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-10-governance); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Mobile (lane governance); repository adoption task ADOPT.10 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-10-governance (python tools/delivery.py claim ADOPT.10.governance --worker <name>); task branch task/adopt-10-governance in Plan; ledger record ledger/tasks/adopt-10-governance.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- GOV.12
Opens when the record is merged: GOV.12, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-10-governance.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.10.release — Adopt Mobile: Release readiness and family release.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-10-release); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Mobile (lane release); repository adoption task ADOPT.10 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-10-release (python tools/delivery.py claim ADOPT.10.release --worker <name>); task branch task/adopt-10-release in Plan; ledger record ledger/tasks/adopt-10-release.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- REL.04
Opens when the record is merged: REL.04, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-10-release.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```

```text
Execute ArcForges adoption slice ADOPT.10.runtime-proofs — Adopt Mobile: Runtime proofs.

Slice record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\adoption.md (anchor task-adopt-10-runtime-proofs); adoption rules ADP-01 to ADP-08: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\adoption.md.
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Repository reviewed: C:\MyFile\Projects\ArcForges\Mobile (lane runtime-proofs); repository adoption task ADOPT.10 records the repository-wide facts once and closes after all of its slices.
Claim and handoff record: claims/adopt-10-runtime-proofs (python tools/delivery.py claim ADOPT.10.runtime-proofs --worker <name>); task branch task/adopt-10-runtime-proofs in Plan; ledger record ledger/tasks/adopt-10-runtime-proofs.md with status complete.

Start prerequisites: [artifact] ADOPT.01: frozen baseline record.
Tasks in scope (classify each exactly once as inherited, inherited with adjustment, gap or conflicting under ADP-02, using only reviewed evidence under ADP-03; bind planned write scopes to the actual layout under ADP-07):
- PRF.10
Opens when the record is merged: PRF.10, except any task this slice classifies as inherited. Every task classified as inherited gets its own ledger/tasks/<key>.md with status inherited (<key> is the task ID in lower case with dots replaced by hyphens) in the same pull request as the slice record, so it never becomes ready. A task inherited with adjustment gets no such record and opens with its remaining scope.

Permitted write scope: Plan:ledger/tasks/adopt-10-runtime-proofs.md; Plan:ledger/tasks/<key>.md (status inherited) for each task in scope classified as inherited
Validation (P2-017, ADP-06): review of merged source, retained CI results and receipts only; no builds, downloads or runtime checks.
Completion evidence for the ledger: one row per task in scope with classification, evidence references, bound write scope, remaining scope, conflicts raised under D-001 and blockers; for each task classified as inherited, its own record with status inherited naming the obligation parts satisfied, the receipts and source commits relied on and the untested coverage carried forward; adjustments that fit no existing task become a planning change. Do not execute implementation tasks during adoption.
```
