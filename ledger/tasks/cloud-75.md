---
task: CLOUD.75
status: complete
recorded: 2026-10-06
claimant: w-codex-20261006-pat
epoch: 1
---

# Required deployment realm and atomic persisted recovery authority

Implementation delivery is complete for CLOUD.75. This is the shared production authority component, distinct from downstream route activation and full-system acceptance. The Final file was not modified.

## Delivered behavior

The sole shared realm snapshot carries required configured realm/AuthEpoch/expected recovery generation and actual persisted recovery revision. Lazy canonical AF_REALM_ID/AF_AUTH_EPOCH/AF_RECOVERY_GENERATION refuses missing or invalid configuration with no default or automatic generation adoption. A shared internal immutable DB-free capture serves authority resolution and CLOUD.21 transport composition without executor/storage cycles. Anonymous health remains lazy and available.

The real Platform-owned bounded named read signs canonical realm as both OwnerScope and typed Scope parameter, checks exact realm/current open state4/generation/positive revision, and refuses malformed/foreign/closed/stale rows. Temporary read errors have bounded retries/backoff/deadline and cancellation. No cached proof authority or invented user epoch column exists.

IRealmAuthorityFamilyPort resolves current authority server-side; only the exact shared Storage factory issues the opaque Platform recovery-current guard. Issuer/family/plan/scope/generation and captured realm/current state/revision are bound. Missing activation, wrong role/shape and forged/cross-factory capabilities refuse before effects. Generic business Platform, receipt/outbox/archive/release privileges remain forbidden. Recovery transitions refuse in the same transaction as all owner mutations/tail effects. Configured AuthEpoch-only rollover requires CLOUD.21 stale-container drain; no D1 AuthEpoch predicate is claimed.

Production retains the generated closed catalogue and unchanged enrollment plans. An internal deeply immutable test catalogue exercises the real issuer/composer/Worker on all SQLite migrations with separately owner-issued Workspace contributions, without public custom SQL/catalogue or a production dummy plan.

## Reviewed source and actual verification

Reviewed scope authority is Design89f1d78803d4803e33ba78569bdd6f225dbd65bd / Plan4e67d1bf0cf6adf27dbe298e490a0ce800bb5984, with CLOUD.72 completion only and no start cycle. [Cloud PR71](https://github.com/ArcForges/Cloud/pull/71) final d2f672de497646e12efa25d69576914df167795d received [independent exact-head approval](https://github.com/ArcForges/Cloud/pull/71#issuecomment-6025783888) from distinct w-codex-20261006-identity. Earlier substantive source and narrow scope/config corrections were independently reviewed; final source is c8706e92d5c734798a5fc4aa0fc6f2cb6d7f3ed3.

Append-only r48/cloud75r2 supersedes pushed unmerged r47/cloud75r1, preserving all193 historical immutable blobs unchanged. Dependency132/policy77/Worker108/image186 memberships and coordinates remain unchanged. Actual locked Wrangler output is306173 bytes, SHA256943bc173a590cdc57e0752a259c09b296ecd5da75f4e9020917520aea6cd69cc.

Actual component checks passed without skips:330 initial managed guard/core/regression cases;273 correction regressions;12 focused Worker read/generator cases;32 required-configuration composition cases. They exercise actual SQLite recovery transitions after prepare, rollback of all affected owner/tail tables, replay/fresh reread, concurrency, unknown late-tail receipt reconciliation without mutation retry, invalid configuration, wrong signed scope before HTTP, unavailable dependency errors, deadline/cancellation and immutable/cross-issuer/plan capabilities. Fakes cover unavailable transport/error/clock only; SQLite is not provider D1/network or OS proof.

Fresh full npm check passes all plan/physical/migration/naming/toolchain/legal/provenance/format/lint/type gates,18 dependency fixtures and752 Worker cases. Ten actual artifact/legal guard cases passed; synthetic image fixtures are explicit packaging component checks. Initial r47 checking exposed a real scope bug and missing RP-10 correspondence, fixed with typed Scope and three substantive test mappings. One existing commerce10ms timing case passed a justified isolated diagnostic and the hosted run; intentional408-before-dispatch/504-after-dispatch behavior and foreign source were preserved. A Markdown CRLF normalization produced no Git diff before successful full checks. No gate was suppressed.

[Exact PR CI37533918108](https://github.com/ArcForges/Cloud/actions/runs/37533918108) passed all applicable retained checks, both source OS jobs, security/analyzers/dependency/architecture, real Native AOT image/Worker and Verify. Earlier failed/superseded runs remain historical, not passing delivery evidence.

## Actual production delivery

Exact head=reviewed claim epoch1 cfba6e8e7445 and live Cloud integration role were verified before fenced merge. PR71 merged as37fc0a75578acf278fe9689fdce69413362a5eba at2026-10-06T21:36:49Z; clean primary fast-forwarded. No redundant integration-owner source review occurred.

[Normal main CI37535120859](https://github.com/ArcForges/Cloud/actions/runs/37535120859) concluded success with both source OS/security jobs, AOT/Worker/Verify and production deployment; proof deployment was not requested. [cloud-0.1.0-ci.277.1](https://github.com/ArcForges/Cloud/releases/tag/cloud-0.1.0-ci.277.1) published at21:46:04Z targeting exact merge. GitHub reports candidate14167002 bytes/SHA2562745dd8e7a983a598ac90b61d5d833454806aa40d8eb6672839eb568d6045800 and deployment.json431 bytes/SHA256e662abd26f31631abcb97ed6155bbdc2f71fdd47cdbad41dae4a08bc1c33da80. No routine candidate/public archive re-download or republish was used.

Required allowlisted artifact cloudflare-evidence-37535120859-1 ID11446377851 was downloaded once. Its receipt binds exact merge/version, deployed2026-10-06T21:45:59.536Z, base https://arcforges.com/api, imageId sha256:745c1a09316b9f6a590108a4e2c0b5ad6fe488ac1e83345a741187d223ef4f9d and provider digest sha256:377cea8f7d73dfd00d2216f6f7081e1a650a9e6a29cfb06a79dd62e9299dff07. Provider log confirms Workeraf7cb02e-34f5-4c17-9adf-eeac4ab48783, existing applicationa0322dd7-048e-435c-bb15-116e6878b104/lite and arcforges.com/api/* route. workers_dev=false/preview_urls=false are preserved. Migration gate is not-applicable for the current production configuration; no D1 migration or inference that other infrastructure is absent.

One bounded read-only postdeployment GET/api/healthz returnedHTTP200, nativeAot=true and exactmerge/version277.1/build37535120859.1. This proves deployed health, not real signed authority route/provider authentication acceptance. No secret values were read or printed.

## Remaining implementation and deferred acceptance

No remaining CLOUD.75 implementation or human-only blocker. CLOUD.21 owns actual signed executor/global factory and required-config activation plus stale AuthEpoch container fence/drain. CLOUD.13/CLOUD.16 compose this delivered recovery guard for sessions/PAT; CLOUD.12 owns provider credentials/proof verification. Actual execution-time expiry is a separately reviewed producer, not a guarantee from captured-time fresh predicates. Whole commercial/provider/network/restore/OS acceptance remains with the relevant implementation/acceptance owners. SQLite, synthetic legal fixtures and health results do not substitute for it.
