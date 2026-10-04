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

## Post-adoption adjustment (2026-10-04)

This is a later adoption adjustment under DLV-22, introduced by the Design governance-chain planning repair [PR 210](https://github.com/ArcForges/ArcForges-Design/pull/210) (Design source head `68827a21b4525660d4f6d2b88c965433ca0dbef6`; the merge commit is retained in the pull request history, since embedding it would change the reviewed head). It does not reopen or replace this completed slice: the front matter, status, recorded date, claimant, epoch and every frozen classification above are unchanged.

| Task | Classification | Evidence and actual source binding | Remaining scope and blockers |
|---|---|---|---|
| GOV.07 | inherited with adjustment (classification unchanged) | ArcScope main `3762518`: `Directory.Build.props` gives every project a `PrivateAssets=all` ArcForges.Build.Policy reference; `Directory.Packages.props` pins `1.0.0-ci.20.1`, which predates GOV.04's engine candidate; the solution is `ArcScope.slnx`; the single active review is `eng/policy/dependency-review.json`; five projects carry locks. | Write scope is now bound beyond `tests/ArchitectureTests/**` and `eng/policy/exceptions.json`: solution entry, exact Build.Policy pin move to the published GOV.06 candidate with the five project locks it changes, dependency policy and review, licence row, provenance, CI wiring (see the graph record). GOV.06 is a new start prerequisite. ArcScope is AGPL, so no RP-03 exception. No security-scanner configuration change is authorized. |
