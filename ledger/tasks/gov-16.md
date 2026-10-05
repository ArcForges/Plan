---
task: GOV.16
status: complete
recorded: 2026-10-06
claimant: w-c20261005-gov16
epoch: 1
---

# Authorization and owner-chain assertion mechanism

- Implementation: [Contracts PR56](https://github.com/ArcForges/Contracts/pull/56), final reviewed source `a8bb55925a99c353d78048368d8de6f69f406323`; [independent exact-head review5860782437](https://github.com/ArcForges/Contracts/pull/56#issuecomment-5860782437) retains the prior full source approval. Four commits rebased on actual CON.05 main with identical patches. Source merge `89fd2c88e2845e83c8378bdf540f9bea634cb2bf`; primary Contracts main cleanly fast-forwarded.
- Outcome: the owned offline assertion mechanism consumes CON.18 operation metadata and preserves pending catalogue entries rather than promoting migration examples to production bindings. Fifty-one independent hostile boundary fixtures cover customer/service principals, organization/bare-user authority refusal, actor/deployment/owner chains and resource/context/connector egress restrictions. Every actor-chain link retains tool restrictions; unclassified fixture egress boundaries refuse.
- Validation: four independent assertion groups and51 fixtures pass; the existing tooling discovery entry invokes the owned suite and emits authorization-boundaries.json. Source/provenance registration and CI evidence upload are narrow supporting additions; no access policy, package identity, runtime handler or enforcement mechanism was substituted.
- Delivery boundary (as recorded 2026-09-28; the completion follow-up below supersedes its last sentence): symbolic fixture credentials and readiness declarations are not authentication, live provider, runtime enforcement or implemented Cloud/DesktopPlatform bindings. Existing CLOUD.11 and PLT.38 producer declarations and exact bound receipts remain required. Complete only after those producers and this task's own real identity/security integration acceptance; no new downstream producer task was started.

- Exact source [PR CI36358312397](https://github.com/ArcForges/Contracts/actions/runs/36358312397) and [Security36358312457](https://github.com/ArcForges/Contracts/actions/runs/36358312457) passed. Original [main CI36358766004](https://github.com/ArcForges/Contracts/actions/runs/36358766004) and [Security36358766018](https://github.com/ArcForges/Contracts/actions/runs/36358766018) passed, including Build/Verify and all NuGet/npm/Maven publishers. Normal candidate `1.0.0-ci.218.1` was promoted; Maven used the accepted `1.0.0-SNAPSHOT` channel tied to that source/candidate. No verification-only version, tag or republish was created.
- Original provider metadata: candidate artifact10944857579 `contracts-candidate-36358766004-1`, archive SHA256 `10841a6d73d3a1a34f113a9336e98e0974770995063f29bea0481f7f4534a901`; owned offline report is retained by naming-evidence artifact10944902050, SHA256 `02f1936abf7bf6a0200248fac5d73392125046abae1eaed71dfef2126c11e209`; Maven deployment receipt10945110833, SHA256 `5180ffb0add3a94c04427c6c9669c4a0db4b29666b3bfb2c6970f8deaf28a631`. Successful original upload jobs are the transfer receipts; no public package-byte download, repeated archive/hash comparison or runtime cycle was performed.

## Completion follow-up (DLV-41), 2026-10-06

Claim: GOV.16 epoch 1 (w-c20261005-gov16), the completion follow-up. The task has no open completion prerequisite: CLOUD.11 is complete (ledger `cloud-11.md`; Cloud #54, merge `d9947f682e9a160d67b1db18f75d4e490bf9b1ea`) and PLT.38 is complete (ledger `plt-38.md`; DesktopPlatform #129, merge `2ffeba338aa990891f63fd5ed3a32c474a7b9252`). Upstream completion alone is not this task's acceptance, so the remaining acceptance was done here: bind the real producer declarations to the reachability matrix and to the owner/deployment identity chain assertions, as a static check over declared metadata (P2-017). Observed means visible on GitHub; claimant-reported means a local run by the claimant.

### Evidence

- **Implementation.** [Contracts #87](https://github.com/ArcForges/Contracts/pull/87), reviewed and merged head `c4448d5d3c7b176626bdbac3e66c0bb56da324ab`, merge commit `330e46bd158bfbb7cdc94c7006565c87e27b1cc6` (`--merge --match-head-commit`). Independent exact-head review: comment 6005355153, `Reviewed c4448d5d3c7b176626bdbac3e66c0bb56da324ab for [GOV.16] epoch 1: approved` (separate reviewer session; same GitHub account as the claimant, so independence rests on the session). No planning repair was needed: every new file is inside `tests/AuthorizationPolicyTests/**`; the one supporting change is six new paths appended to `eng/provenance/files.json` (the same registration the original delivery made), with no receipt reseal, dependency, workflow or security-check change.
- **What it adds.** (1) `producer-declarations.json`: a reviewed snapshot of the facts the producers declared, each pinned to an exact repository, commit and per-file sha256. Cloud at `d9947f68`: the physical identity, device and workspace tables with their owner relations and uniqueness, the four distinct identifier types, the eight identity plans and the `account-enrollment` family. DesktopPlatform at `2ffeba33`: the fourteen decision steps, four enforcement points and the steps each runs. Contracts reads no producer source and has no cross-repository dependency. (2) `binding-classification.json` and `binding_reachability.py`: all 49 registered `identity.*`, `workspace.*` and `device.*` operations are classified against user, authentication identity, session, device, workspace, API token and flow. The check fails on an operation without a binding (or a stale or duplicate entry), an unknown binding, a binding the producer does not declare or whose owner relation does not reach the user, membership, role, seat, invitation, organization or service-principal vocabulary in the declared model, an authentication identity not distinct from the user, any tool actor on these operations, a non-owner profile, an automation token that mutates, and a plan whose access contradicts the operation's idempotency. (3) Every owner/deployment chain obligation is bound to a verified producer fact, a declared port, or a named pending producer. (4) The report is now `authorization-boundary-evidence.v2` (matrix, fixtures, binding matrix, producer pins, obligations, limits), uploaded by the existing CI step.
- **Observed, hosted CI on the reviewed head `c4448d5`:** all checks passed (Build candidate, Verify, Secret scan, four CodeQL jobs, Dependency review).
- **Claimant-reported, local (Windows 11, Python only):** the owned suite, 36 tests, passes; it includes the negative cases above and stale-pin cases (every pinned source of both producers moved, declared facts changed with the digest unchanged, hand-edited facts, branch, short, extra and missing pins). Two deliberate breaks of the checker (tool-actor check disabled; owner-relation check disabled) each made tests fail. `python tests/AuthorizationPolicyTests/producer_declarations.py verify --cloud <Cloud> --platform <DesktopPlatform>` re-derived both producers' facts from the exact pinned commits (read through `git show`, never the working tree) and found them equal. 62 tooling registration and operation-scope tests, provenance and naming checks, and the prettier check passed.
- **Main push `330e46b`:** run 37388554007 (CI) concluded `success` (job status only): Build candidate, Verify, and the NuGet, npm and Maven channel publishers all `success`; run 37388553541 (Security) concluded `success`. Nothing was downloaded; no tag or republish was made.

### How the pins work and their limit

The pins are source-digest snapshots. CI validates them only for internal consistency (exact commits, the sanctioned source set, facts bound to their digest) and needs no producer checkout or network. They are checked against the producers only by the explicit local `verify` run above, which was run once at the pinned commits; no hosted job re-derives them. No published package carries these facts today, so a source-digest pin is the only sanctioned form (the same shape as the frozen Design oracle in `eng/operation-scope-manifest.json`). A producer that moves must be re-pinned through a reviewed change.

### Owner/deployment chain: what is bound and what is not

| Obligation | Status | Basis |
|---|---|---|
| userSession | bound | Cloud `identity_session` owner relation to the user; actor identity step at the transport boundary and service decision points |
| workspaceOwner | bound | `workspace_workspace.owner_user_id` relation and `(realm, owner)` uniqueness; scope step at the service decision point |
| currentPermission | bound | capability-permission step at the service decision point; owner validation step at the owner final validation point |
| separateOperatorIdentity | bound | operator session and access tables exist and do not reference the user table |
| currentServiceEligibility | **port only** | The owner validates last, but eligibility is a fact the host owner validator supplies through a port. No producer declares an eligibility source or a production implementation of that port. |
| recheckAtTrigger | **pending-producer** | No producer declares an automation trigger that re-evaluates its owner. The pinned Platform pipeline runs when a request is made. |
| explicitProvisioning | **pending-producer** | No producer declares a deployment-service provisioning record. The pinned enrollment family provisions a user workspace, not a deployment service. |

`recheckAtTrigger` and `explicitProvisioning` have no owning task in the delivery graph. They are a candidate planning follow-up for the Architecture Owner (D-001), not something this task could close or invent a substitute for. The offline hostile fixtures from the original delivery still assert the intended behaviour (automation loses authorization when its owner loses permission or service eligibility even with a valid process credential; no customer service principal or Organization authority exists), as symbolic decisions, not as producer behaviour.

### Why this is complete

GOV.16's own acceptance is a static reachability matrix over the declared catalogue, hostile actor-chain fixtures, and an asserted owner/deployment identity chain, over declared metadata and not live-system testing (P2-017). The matrix and fixtures were delivered earlier. This follow-up adds the identity, workspace, device and session classification of every identity-bearing operation and binds the chain obligations to the real CLOUD.11 and PLT.38 declarations, with every gap stated rather than promoted. The unbound items above are limits of what producers declare today, not unmet acceptance of this task.

### Not observed and not claimed

- Declared metadata only: no operation handler, store, runtime enforcement point or live provider is bound to any operation. Every classified operation reports `behavior: not-bound`.
- Cloud's device, session, API-token and flow behaviour belongs to later producer tasks; their classifications rest on declared tables only.
- Linux and macOS runtime, hosted device, GUI, browser, live-service and installed-consumer behaviour, real authentication and real enforcement were not observed. gitleaks was not run locally (the hosted Secret scan passed). The full `tests/tooling` suite and the package build ran in hosted CI only.
