---
task: ADOPT.05.app-composition
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
| APP.02 | gap | E1: no matching product implementation or acceptance receipt in frozen inventory. | ArcScope:src/ArcForges.ArcScope.Application/**; ArcScope:src/ArcForges.ArcScope.Infrastructure/**; ArcScope:tests/** | Real read/create/append annotation commands through typed application handlers and local persistence, with descriptor/risk/context validation and one write path shared by UI and own-app capability invocation. Professional ArcScope completion remains WP33-WP35. Evidence required: Source commit, command receipt samples, validation-failure cases. | No D-001 conflict identified. Prerequisites: APP.01, PLT.24, PLT.38. |
| APP.03 | inherited with adjustment | E3: package-based Hello AOT host exists; typed host-port product composition and command/owner-refusal proof absent. | ArcScope:src/ArcForges.ArcScope/**; ArcScope:packaging/** | A clean Native AOT ArcScope consumer built purely from published Platform/Contracts packages and in-process typed host ports; no source reference or local-RPC product loop. Package-only restore, publish/run, command/cancel/result and owner refusal proven. Evidence required: AOT publish log, package hash manifest, command/cancel/result and owner-refusal test results. | No D-001 conflict identified. Prerequisites: APP.01, APP.02, PRF.04, NAT.01. |

All obligation parts, tests and gates remain required; the outcome summary does not replace the prompt. No task is fully inherited, so no inherited task record is created. Reuse existing mechanisms while adding the missing outcome. Readiness still requires the listed prerequisites and the authoritative ledger. No extra repository-wide barrier is added. No removed-product cleanup performed or certified; preserve historical provenance. Validation: source/receipt review and explicit-root delivery.py check only, with no new builds, downloads or runtime cycle. Runtime/device/macOS/commercial acceptance is untested by adoption. Exact-head review and ledger merge are recorded in the claim and PR. Unselected implementation tasks are classified but not claimed.

