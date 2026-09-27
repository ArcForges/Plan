---
task: ADOPT.05.governance
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
| GOV.07 | inherited with adjustment | E2: baseline licence/dependency/provenance policies exist; shared engines and complete naming/contract/banned-API fixtures absent. | ArcScope:tests/ArchitectureTests/**; ArcScope:eng/policy/exceptions.json | ArcScope enforces its own layering/licence/naming/banned-API/contract-consumption rules independently. Evidence required: Per-rule pass/fail fixture table for ArcScope's project graph. | No D-001 conflict identified. Prerequisites: GOV.04, GOV.05. |

All obligation parts, tests and gates remain required; the outcome summary does not replace the prompt. No task is fully inherited, so no inherited task record is created. Reuse existing mechanisms while adding the missing outcome. Readiness still requires the listed prerequisites and the authoritative ledger. No extra repository-wide barrier is added. No removed-product cleanup performed or certified; preserve historical provenance. Validation: source/receipt review and explicit-root delivery.py check only, with no new builds, downloads or runtime cycle. Runtime/device/macOS/commercial acceptance is untested by adoption. Exact-head review and ledger merge are recorded in the claim and PR. Unselected implementation tasks are classified but not claimed.

