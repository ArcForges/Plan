---
task: ADOPT.05.simulator
status: complete
recorded: 2026-09-27
claimant: w-20260927-arcscope-lane
epoch: 1
---

## Reviewed inputs

Frozen ArcScope a6899eddc4da7cf338d1a1404f1c0c1b8acc546d and Design 722e85641c8afb765dafcab5bc0e84d5a22d5a3c. See [repository evidence and layout binding](../adoption/ArcScope.md) for E1-E5 and exact retained CI/publication. Each task was compared against its current outcome, mapped obligation parts, write scope, validation and required evidence; no bootstrap is inherited as completed product behavior.

## Classifications

| Task | Classification | Evidence | Planned write scope (bound in repository record) | Remaining outcome and evidence | Conflicts / blockers |
|---|---|---|---|---|---|
| SIM.06 | gap | E1: no matching product implementation or acceptance receipt in frozen inventory. | ArcScope:src/ArcScope/ArcScope.Acquisition/Adapters/Simulation/**; ArcScope:src/ArcScope/ArcScope.Desktop/Simulation/**; ArcScope:tests/ArcScope.Tests.Integration/Simulation/** | A SimulatedDataSource adapter feeds the ordinary ArcScope acquisition pipeline; simulated data is usable in every normal ArcScope workflow (session, capture, decoder, measurement, report) while remaining labelled synthetic everywhere, including through export/copy; with realtime disabled, a client reaches the same state via the polling fallback. Evidence required: native ingestion and synthetic-labelling results | No D-001 conflict identified. Prerequisites: SIM.05, CON.21, SCOPE.01, SCOPE.14, SCOPE.24. |

All obligation parts, tests and gates remain required; the outcome summary does not replace the prompt. No task is fully inherited, so no inherited task record is created. Reuse existing mechanisms while adding the missing outcome. Readiness still requires the listed prerequisites and the authoritative ledger. No extra repository-wide barrier is added. No removed-product cleanup performed or certified; preserve historical provenance. Validation: source/receipt review and explicit-root delivery.py check only, with no new builds, downloads or runtime cycle. Runtime/device/macOS/commercial acceptance is untested by adoption. Exact-head review and ledger merge are recorded in the claim and PR. Unselected implementation tasks are classified but not claimed.

