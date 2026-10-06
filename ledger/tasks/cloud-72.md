---
task: CLOUD.72
status: complete
recorded: 2026-10-06
claimant: w-codex-20261006-identity
epoch: 1
---

# Production Identity persistence, identifiers and enrollment family composition

Implementation delivery is complete for CLOUD.72's bounded production persistence and identifier contribution to WP-22.00. The existing model, rules, service and original family remain owned by completed CLOUD.11. This record distinguishes actual component and delivery evidence from remaining system composition and whole-series acceptance.

## Delivered behavior

- The internal `D1IdentityStore` executes every core named plan through the Abstractions owner plan port. Complete user, credential, recovery and personal-workspace projections are realm-bound. Credential enumeration uses 64-row `(created_at, auth_identity_id)` keyset pages without a silent total cap. Malformed/foreign rows, stale generations, defects, constraints, guard refusal and unknown outcomes remain distinct; bounded temporary read/receipt retries preserve cancellation.
- The production identifier source uses cryptographic version-4 UUIDs in canonical lower-case form. Primary keys and revision-zero guards prevent overwrite; allocation collisions retry with fresh identifiers after whole-batch refusal.
- Enrollment inspects the original command receipt before the existing-credential shortcut. A stable caller-sensitive fingerprint includes the full supplied credential/profile content and excludes attempt identifiers/time. Same-content replay returns the original stored user, credential and workspace with `CreatedUser=false`; changed-content reuse and expired receipt identifiers are denied. Unknown outcomes inspect and retry only the same command with bounded backoff. Actual committed lost responses create one user/workspace/event.
- The generic family bridge accepts only opaque owner-bound contribution capabilities issued by the same factory for the exact registered family/plan, validates all required roles before effects, and uses the existing family executor and fixed SU-04 order. Forged, foreign, cross-factory, wrong-plan and incomplete capabilities are refused. Same-owner disjoint contribution subsets compose without foreign-owner permission. The enrollment exception remains limited to the exact personal-workspace creation plan and two ownership lookup reads. Generic Platform participation remains forbidden; ordinary modules receive no receipt/outbox/archive/release capability.
- Identity's own registration binds the real store, identifier source and service; actual module composition is tested with the real executor supplied. Necessary owner-bound read plans and complete projections are generated into both manifests. No table or migration is added.

## Reviewed source and input admission

- Scope repairs were merged through the separately independently reviewed Design/Plan pairs; final exact fixture/decoder authority is Design `e4ec7c979a1af7135999094672d02a5eb55b2472` and Plan `7972e1e84466b67285e6b07702ac2a4d68c257a7`. The Final launcher file was not modified.
- [Cloud PR #68](https://github.com/ArcForges/Cloud/pull/68) was independently reviewed by distinct worker `w-codex-20261006-pat`: [complete source approval](https://github.com/ArcForges/Cloud/pull/68#issuecomment-6022254053), [rebased/admission approval](https://github.com/ArcForges/Cloud/pull/68#issuecomment-6022710699), [final semantic/input approval](https://github.com/ArcForges/Cloud/pull/68#issuecomment-6023463611), and [exact final formatting delta approval](https://github.com/ArcForges/Cloud/pull/68#issuecomment-6023486780) for `0a53eb783c39b339df8628ff39df862b1b7c2677`. No redundant integration-owner source review occurred.
- Immutable `cloud-release-r44`, `cloud-72-r3`, and task-prefixed runtime-notice/Worker records retain all r43/r2 predecessors and accepted COM.01 inputs/coordinates. Owner source is `0b0fd5d8301c37cb82a312486f7ea6c72c1b052f`. The dependency closure remains 132, with 77 current admission, 107 Worker and 174 image input hashes independently checked. Two never-merged r39 records were archived byte-identically under the owned artifact-profiles directory; accepted historical evidence was not edited or removed.
- Actual locked Wrangler output SHA-256 `10b5ef43fbbb9e45162e0f8401f9f556472d5f94617b596f72809668200606a9`, 283,552 bytes, 107 parsed/38 emitted inputs. No dependency coordinate, runtime/provider pin, licence classification or security gate is weakened.
- CI findings were diagnosed and fixed: exact retained keyset/inventory/bundle expectations; Linux using order; a test property misleadingly named `password` although it contains a stored versioned salted verifier. The final `passwordHash` support/fixture/vector/decoder labels preserve all eight expected plan argument arrays and fingerprint bytes. No detector suppression or password-cryptography relaxation occurred. The last two mutable metadata corrections preserve parsed JSON and every immutable record/input byte.

## Actual verification

Claimant-reported Windows component checks used the shared workstation build slot where required:

- 220 managed Identity/family/layer cases passed, including complete actual D1 store and module DI composition over real Worker SQLite plans/migrations, collision rollback, realm isolation, concurrent enrollment, and lost responses before/after commit. Fake ports cover only unavailable dependency errors, cancellation, bounded retries, unknown outcomes, malformed/foreign rows and complete pagination. Cryptographic identifier stress covers 20,000 concurrent draws.
- Final changed-component checks: 29 actual SQLite core cases, two actual shared-vector commit cases, 12 managed decoder/argument cases, and 28 dependency/artifact cases passed without skips. Scoped production format and all changed TS/JSON formatting passed. Artifact legal-image cases use explicit synthetic fixtures and are not real AOT/OS evidence.
- One explicit local workerd/D1 run passed four scenarios and 25-round enrollment/link/revocation races. Evidence SHA-256 `79ee5c5d62677b89a46676f6fe47eb50ca0e300caa73dfa4cc6e1d3bba491ea1`. This is actual local workerd evidence, not Cloudflare REST/network or provider-authentication evidence.
- Observed exact final [PR CI 37516445611](https://github.com/ArcForges/Cloud/actions/runs/37516445611) passed both source OS jobs, dependency/architecture/security gates, all four analyzers, the synthesized security gate, real Native AOT image inspection/Worker build and Verify. Ubuntu source logs show 18 dependency cases, 736 Worker cases and 1,172 managed/architecture cases passing, with zero managed skips. Earlier failed/superseded runs are retained and are not represented as passing delivery evidence.

## Integration, production publication and deployment

- Fresh claim `claims/cloud-72` at `c471c9d7fce63df182ee8c1a30ac4d91585efb54` had exact head=reviewed `0a53eb7`; held `integration:Cloud` epoch 1 receipt `3a73dd2a6960c05034d1a99dc8e0a33ac80b0e94` was verified before the fence. Previous COM.01 normal publication/deployment was already terminal success.
- PR #68 merged with the reviewed-head fence as `278894103207ea3318eed72a3618fb641837c488` at 2026-10-06T19:15:42Z. Cloud primary main was fast-forwarded cleanly. Separate Cloud/Plan task branches and retained worktrees remain.
- Observed [main CI 37517629818](https://github.com/ArcForges/Cloud/actions/runs/37517629818) concluded success with both source OS/security jobs, actual AOT/Worker/Verify and normal Cloudflare deployment passing. Proof deployment was not requested.
- Published [cloud-0.1.0-ci.264.1](https://github.com/ArcForges/Cloud/releases/tag/cloud-0.1.0-ci.264.1) at 2026-10-06T19:23:50Z, targeting the exact merge. GitHub reports the candidate asset size 14,107,614 and SHA-256 `823c46d7e92fb88d5b5ab5a001e032d6fa7dbfc5a4a72d5d2c8e9a3ee7d54ab3`; the ordinary 431-byte deployment receipt SHA-256 is `6c6414a7670e63ee6a8cb5e04b494e7aa611eb7f02ab4d6bc2a2ed0dc81b4936`. No routine candidate archive download or new republish was used for verification.
- Downloaded the required allowlisted evidence artifact `cloudflare-evidence-37517629818-1`, ID `11437638171`, and verified the deployment receipt: exact merge, version `0.1.0-ci.264.1`, deployed 2026-10-06T19:23:45.932Z, base `https://arcforges.com/api`, image ID `sha256:62b2450d76169e9ce966d698edbb765771cfff709b079f4b21180c96b2d834eb`, provider image digest `sha256:7f5ac416f1ec71239762217d4688f52173bcbd5f395adadea8bb7042e4d98c61`.
- Provider deployment log records Worker version `de0348a3-9aac-4fba-8bfd-621a4f03b574`, unchanged route `arcforges.com/api/*`, existing Container application `a0322dd7-048e-435c-bb15-116e6878b104`, and unchanged `lite` configuration. Checked-in `workers_dev=false` and `preview_urls=false` are preserved. The migration gate reports `not-applicable` for the current production configuration; this task performed no production D1 migration and makes no claim that other account infrastructure is absent.
- One read-only postdeployment GET `/api/healthz` returned HTTP 200, `nativeAot=true`, exact merge, version `0.1.0-ci.264.1` and build `37517629818.1`. No secret values or local credentials were read/printed. This verifies deployment health, not live Identity endpoint or provider authentication acceptance.

## Remaining implementation and deferred acceptance

No remaining CLOUD.72 implementation or human-only blocker. System composition remains with its actual owners: CLOUD.21 activates the default production executor/generation configuration and protected route composition; CLOUD.12 implements method/provider authentication and mail; CLOUD.13 implements sessions/devices; CLOUD.19 implements browser origin/CSRF and catalogue/ingress lifecycle. This record does not mark those producers complete.

Whole-series commercial, actual external-provider/network, live authentication and OS-isolation acceptance remain deferred to those implementation/acceptance owners. All feasible ordinary CLOUD.72 components have been exercised; unavailable dependencies were faked only in explicit error/contract tests. Local SQLite/workerd, synthetic legal fixtures and the health route are never presented as proof of real provider behavior or OS isolation.
