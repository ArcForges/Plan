---
task: PLT.17
status: complete
recorded: 2026-09-28
claimant: w-20260927-mobile-lane
epoch: 1
---

# Application identity and explicit composition

- Implementation: [DesktopPlatform PR73](https://github.com/ArcForges/DesktopPlatform/pull/73), final reviewed head `37f3fc27f00c0549b1767c04d6bd27a16136da4c`, independent final approval [5860750077](https://github.com/ArcForges/DesktopPlatform/pull/73#issuecomment-5860750077). Source merge `cdd16cf5ed8b505779facf8bb55f18d95ba7cdcd` followed the exact approved green head and claim fence. Original main publication is recorded below; the integration owner confirmed a clean primary fast-forward.
- Outcome: ArcForges.Capabilities supplies closed `arcscope`/`companion` product identities, immutable installation/instance identities using published strong IDs, and explicit generic owner factories and per-composition typed handler registrations. Companion retains one product identity across platforms. The full uint64 epoch range is supported, including zero; an absent epoch or default strong ID is refused.
- Refusal behavior: missing target fails validation; foreign product/device/installation and foreign handler registration fail authorization; stale instance/epoch and stopped roots fail as gone before handler admission. Refusals use existing Foundation errors, no effects and no automatic retry. Start creates a fresh process instance, while the host owns durable installation state and authoritative epoch allocation. Stop fences later admission without erasing identity or claiming rollback of admitted effects.
- Eight deterministic offline tests pass: closed products, invalid/missing identity parts, owned generated ApplicationScope copies, separate session/history/capability fixture state, missing/foreign/stale targets, concurrent/restarted instances, stop with an admitted pending effect, and cancellation before admission. Tests use real typed handlers and immutable IDs. The final full solution Release rebuild with emitted generator files succeeds using existing SDK10.0.401 and invocation-only10.0.11 trim/AOT adapter; official CI remains pinned10.0.400.
- Exact [PR gate36358125570](https://github.com/ArcForges/DesktopPlatform/actions/runs/36358125570) passed all12 checks, including the full evaluated architecture policy and native/managed candidate packaging.
- GOV04 final-base integration adds exactly two actual project classifications and six real public-method-to-behavioral-test bindings. Local evaluated architecture policy found no API-binding/project violations; expected canonical naming/secret and same-source native receipt findings were left to official CI. Both Capabilities and Security workflow test steps are retained.
- Supporting admission: new package/test entries preserve existing Foundation/Contracts dependency versions and hashes, with33 dependency entries/207 inputs and the PLT36 immutable predecessor retained. Provenance427 files passes; existing licence ownership, runtime ownership, release allowlist and active reconciliation inventory include the two real projects. Explicit typed delegates require no reflection activation, dynamic service locator or global product registry.
- Limits: trusted in-process composition acceptance only. No Android/Web execution, installed consumer, product persistence, device registration, authentication, grant validation, remote transport or security sandbox claim. Hosts must supply independently scoped concrete stores and must not deliberately share them. These remain the named runtime owners' work, rather than substitutes introduced into this task.
- Ledger exact review and merge identities are retained in the claim and Plan PR history. Branches and worktrees are retained.


- Original [publication36358523690](https://github.com/ArcForges/DesktopPlatform/actions/runs/36358523690), run32 attempt1 at source `cdd16cf5ed8b505779facf8bb55f18d95ba7cdcd`, passed all candidate jobs and publisher `108731977682`. All seven NuGet pushes succeeded, including new `ArcForges.Capabilities` at `1.0.0-ci.32.1`. Original candidate `nuget-candidate-36358523690-1`, artifact `10944881884`, digest `sha256:46b0a6dfa8ce4bca76a5996dd862140a9b81e2cf226678855b21c9d6bf3eddb4`, retains the individual package manifest hashes. These are original job and artifact metadata receipts; no public package bytes were downloaded for routine verification. No completion prerequisites remain.

