---
task: PLT.59
status: complete
recorded: 2026-10-06
claimant: w-codex-20261006-coord
epoch: 1
---

# Managed security and content-helper production publication

PLT.59 completes its current implementation and publication deliverable. The task has no completion prerequisites. The seven existing complete managed producers are now admitted and published through the normal immutable package cohort; this does not certify native parser RIDs, OS isolation, installed consumers or whole-product acceptance.

## Preserved earlier repair

The deterministic stage-integration fixture clock repair remains accepted in DesktopPlatform [PR 152](https://github.com/ArcForges/DesktopPlatform/pull/152), exact head `985f00d284301941d83c4279cab59e515ca33a8e`, merged as `56243df6ef505bb84968409d08c814ed9d86abda` at 2026-10-06 17:46:13 UTC. Its 47 actual stage-integration tests preserved freshness and expiry negatives. The later package activation preserves that source and all historical Contracts113/270 fixtures and immutable evidence; it does not redo or replace the earlier repair.

## Source, independent review and applicable CI

- DesktopPlatform [PR 158](https://github.com/ArcForges/DesktopPlatform/pull/158) delivered exact head `ca53a6d2213429d32d3017002c455a5ec6a012dd`, fenced-merged as `aa3ef3b48c3a8eb5ee240f4ffcbdfcf4febbeac3` at 2026-10-06 21:25:37 UTC.
- Independent audit worker review covered the complete producer and admission at `85463fda5ba905a99562c6cc0a03ddae15c43853`: [full approval](https://github.com/ArcForges/DesktopPlatform/pull/158#issuecomment-6024871860). The only subsequent delta changed the explicitly admitted `AssistantAbstractionsPackageGuards.external_version` fixture from Contracts216 to the actual admitted Contracts324, preserving every dependency assertion and missing/extra/repin negative: [exact delta approval](https://github.com/ArcForges/DesktopPlatform/pull/158#issuecomment-6025298379), [canonical final-head reaffirmation](https://github.com/ArcForges/DesktopPlatform/pull/158#issuecomment-6025754493). Independence is by separate worker session, despite the shared GitHub account.
- Exact-head [PR gate run 37530211699](https://github.com/ArcForges/DesktopPlatform/actions/runs/37530211699) completed successfully; all 22 retained jobs passed. Source, policy, dependency, licence, provenance, secret-scan, managed packaging, native and Native AOT compile gates remained applicable and enabled.

## Implemented production delivery and component evidence

The normal registry now includes the complete existing `ArcForges.Security`, `ArcForges.Security.Secrets`, `ArcForges.Security.Audit`, `ArcForges.Security.LocalRpcBoundary`, `ArcForges.Security.CapabilityEnforcement`, `ArcForges.ContentSandbox.Contracts` and `ArcForges.ContentSandbox.Broker` producers. Their real security, credential, durable audit, guarded capability, parent-side helper contracts and lifecycle implementations are published; interfaces or success-returning placeholders were not substituted. Product consumers continue to use exact published packages rather than sibling source dependencies.

The older Contracts216 peer closure could not compose with ArcScope's actual Contracts324 producer. The implementation binds the affected production peers and regenerated locks to the already published compatible Contracts324 closure. Existing SDK verification established the five actual Contracts324 archives, signatures and source association from Contracts publication330; the retained `artifacts/plt59-producer-integrity.json` records their verified archive hashes. No second public-artifact download or installation cycle is represented here.

Actual local SDK10.0.400 evaluated restore and Release build passed with zero warnings or errors. The complete component run had 1,336 successes: security928, secrets34, durable audit53, capability79, helper161 and persistence81. Fifteen explicit OS opt-ins were skipped and remain outside this component evidence. All 22 managed entries passed actual generated dependency and strict managed/legal asset checks. The admission binds 62 NuGet coordinates, 10 Python coordinates and 289 input paths; source provenance1045/144, licence63 and 38 adversarial dependency/licence cases passed. The final two focused packaging guards passed after the exact fixture correction. These results are retained source/component evidence, not installed-package or OS acceptance.

The secret scanner admits only the three exact new Secrets project-hash line successors, retaining the old patterns and exact rule/path/line boundaries. Existing package identities, native producers, immutable receipts, warning/error gates and historical fixtures remain intact.

## Actual normal publication

Normal main-push [Publish NuGet run 37533808648](https://github.com/ArcForges/DesktopPlatform/actions/runs/37533808648), exact source `aa3ef3b48c3a8eb5ee240f4ffcbdfcf4febbeac3`, completed successfully; all 24 jobs passed. Its [publisher job 112515866124](https://github.com/ArcForges/DesktopPlatform/actions/runs/37533808648/job/112515866124) rechecked the source identity, allowlist, contents and hashes before authentication and pushed the same verified package bytes to nuget.org.

The actual single-version cohort is **1.0.0-ci.110.1**, comprising 22 managed packages plus Build.Policy and the existing Image win-x64 runtime. Publisher logs contain 24 `Created` responses and 24 successful push receipts, from 21:42:13.5787757 through 21:42:36.2312212 UTC on 2026-10-06. All seven newly activated producers have successful push receipts within that run. Diagnostic component packs were not used as proof of publication. No tag, republish, extra consumer installation or runtime acceptance cycle was performed for this ledger.

## Deferred acceptance and follow-up owners

- PLT.46 and PLT.54 retain the broader security/loader closure and actual OS integration acceptance. The skipped OS opt-ins are not converted into passed isolation or credential-store checks.
- APP.02/APP.03 retain actual product and shared-assistant composition and acceptance using the published exact cohort.
- NAT.22/NAT.25 retain native/runtime publication and parser RID work. Publishing the existing Image win-x64 cohort member does not establish other RIDs or parser behavior.
- Installed-consumer, executable signing, all-RID isolation and whole commercial/system acceptance require their actual owner evidence. This completed managed producer delivery has no remaining implementation or human-only blocker; those independently owned checks remain deferred.
