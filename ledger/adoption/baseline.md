# Frozen adoption baseline

Recorded 2026-09-27 for ADOPT.01, under Design P2-018, P2-020 and ADP-09.

This snapshot records instruction alignment and existing publication metadata. It does not classify implementation as inherited or certify product behavior. The historical accepted baseline remains WP00–WP03.02; WP03.03 had not started. Each adoption slice must compare its tasks with these frozen inputs and record its own classification. Removed-product source cleanup remains with CON.23, GOV.17 and GOV.18.

## Authorities and evidence method

- Design authority: `722e85641c8afb765dafcab5bc0e84d5a22d5a3c` in ArcForges-Design.
- Plan execution authority before this ledger: `35d3d2768b79ed8febf56cc699fb5c7d32e7d348`.
- Each instruction PR was independently reviewed at its exact head and merged only after applicable PR CI succeeded. The repository sections below retain reviewed and merge commits.
- Publication evidence uses original CI/provider receipts and registry or release metadata, without downloading published artifact bytes. Candidate availability is distinct from runtime or commercial acceptance.
- The instruction retarget and baseline inspection required no local product build, runtime, device, browser, installed-consumer, live-service, Workflow or inference validation. Mobile's necessary CI tooling repair additionally ran strict Gradle formatter verification and seventy offline policy tests, recorded with its evidence below; no local Android product build was performed.
- The user superseded the earlier network-stop instruction for this execution: transient Git/TLS failures are diagnosed and retried without proxy or network changes. An actual interactive credential requirement remains a manual-action boundary.
- Necessary CI repair decision: Mobile's existing retained Android lint gate rejected the previously pinned Spotless `8.10.2` because `8.10.3` was available. The user's authorization to resolve routine problems and merge only green CI covers the minimal tooling patch, associated strict verification metadata and admission/resource-profile records in the same retarget PR. This is an explicitly recorded implementation-scope exception needed to make the authorized PR mergeable; it changes no product behavior, identity, archive expectation or adoption classification. The complete changed head received independent peer review and all retained CI remained required.

## Repository snapshot

Repository details are recorded below after their required main publication completes.

### DesktopPlatform

- Frozen main / retarget merge: `e5ce94221c13d0014781a760c0865b942350be4d`; [PR #64](https://github.com/ArcForges/DesktopPlatform/pull/64).
- Reviewed head: `1657b2e505dec55d5fb60f485c2f727d7091a722`; [independent approval](https://github.com/ArcForges/DesktopPlatform/pull/64#issuecomment-5857666552). All twelve retained PR checks succeeded.
- Open PRs: none. Complete remote branch inventory: `main` = `e5ce94221c13d0014781a760c0865b942350be4d`; `task/adopt-01` = `1657b2e505dec55d5fb60f485c2f727d7091a722`. Clean primary fast-forwarded; task worktree retained.
- Main publication [run 36334843593](https://github.com/ArcForges/DesktopPlatform/actions/runs/36334843593): receipt pending; candidate is not yet frozen as published.

### Contracts

- Frozen main / retarget merge: `b10b2f6f316bf0c007e00632c5442fc102ebbe6e`; [PR #44](https://github.com/ArcForges/Contracts/pull/44).
- Reviewed head: `a3c3e5e48d8da4b3ff2e560d3bb6352cca475156`; [independent approval](https://github.com/ArcForges/Contracts/pull/44#issuecomment-5857667708). All retained applicable PR checks succeeded.
- Open PRs: none. Complete remote branch inventory: `main` = `b10b2f6f316bf0c007e00632c5442fc102ebbe6e`; `task/adopt-01` = `a3c3e5e48d8da4b3ff2e560d3bb6352cca475156`. Clean primary fast-forwarded; task worktree retained.
- Main publication [run 36334951174](https://github.com/ArcForges/Contracts/actions/runs/36334951174): receipt pending; candidate is not yet frozen as published.

### ArcScope

- Frozen main / retarget merge: `a6899eddc4da7cf338d1a1404f1c0c1b8acc546d`; [PR #17](https://github.com/ArcForges/ArcScope/pull/17).
- Reviewed head: `4815b61b45a5270c1df8fc90cee55d65e69fa83e`; [independent approval](https://github.com/ArcForges/ArcScope/pull/17#issuecomment-5857667131). All retained applicable PR checks succeeded.
- Open PRs: none. Complete remote branch inventory: `main` = `a6899eddc4da7cf338d1a1404f1c0c1b8acc546d`; `task/adopt-01` = `4815b61b45a5270c1df8fc90cee55d65e69fa83e`. Clean primary fast-forwarded; task worktree retained.
- Main publication [run 36335032606](https://github.com/ArcForges/ArcScope/actions/runs/36335032606): receipt pending; candidate is not yet frozen as published.

### Cloud

- Frozen main / retarget merge: `60c5c4288b126c81a09fa5d1944671e9acb87495`; [PR #22](https://github.com/ArcForges/Cloud/pull/22).
- Reviewed head: `4f37ac16ec70ca421bc227c0c448fb424e5df53f`; [independent approval](https://github.com/ArcForges/Cloud/pull/22#issuecomment-5857674197). All eleven retained applicable PR checks succeeded.
- Main publication [run 36335115598](https://github.com/ArcForges/Cloud/actions/runs/36335115598): receipt pending; candidate is not yet frozen as published.
- The private npm workspace does not publish an npm library. Candidate registry scope is the Cloudflare container/Worker and the GitHub release with its original deployment receipt.

### AI

- Frozen main / retarget merge: `31f734d7b8aece5f1c87cfda9d5c6ce420bcfc40`; [PR #22](https://github.com/ArcForges/AI/pull/22), merged 2026-09-27T16:42:47Z.
- Reviewed head: `cdb1264bc4d89ab9014c3795f53e28256e54f4b8`; [independent approval](https://github.com/ArcForges/AI/pull/22#issuecomment-5857672617).
- Open PRs: none. Complete remote branch inventory: `main` = `31f734d7b8aece5f1c87cfda9d5c6ce420bcfc40`; `task/adopt-01` = `cdb1264bc4d89ab9014c3795f53e28256e54f4b8`. Primary checkout clean and current; task worktree retained.
- [Main CI 36334249591](https://github.com/ArcForges/AI/actions/runs/36334249591) succeeded: source/offline units, security, both CodeQL jobs, Build candidate, Verify, Deploy Cloudflare and Verify deployment. Main dependency review was correctly skipped.
- GitHub Releases / Cloudflare latest candidate: [ai-0.1.0-ci.68.1](https://github.com/ArcForges/AI/releases/tag/ai-0.1.0-ci.68.1), published 2026-09-27T16:44:38Z, targeting frozen main. The workspace is private; this is not an npm library publication.
- Original release asset metadata: `ai-worker.zip` ID `593330244`; `candidate.json` ID `593330242`; `deployment.json` ID `593330246`. [Deployment receipt job](https://github.com/ArcForges/AI/actions/runs/36334249591/job/108662189499) succeeded for the verified bundle and prerelease; [Verify deployment](https://github.com/ArcForges/AI/actions/runs/36334249591/job/108662252958) also succeeded. No asset bytes were downloaded.
- Evidence observed 2026-09-27T16:51Z. No runtime, Workflow or inference tests were performed; provider completion is not product acceptance.

### Web

- Frozen main / retarget merge: `b0a6d7e1552d0a28f6abc30978cc25b7da3a8461`; [PR #19](https://github.com/ArcForges/Web/pull/19), merged 2026-09-27T16:51:10Z.
- Reviewed head: `5276f166a594b7cdf91733f80b8e87452c4c6224`; [independent approval](https://github.com/ArcForges/Web/pull/19#issuecomment-5857675560).
- Open PRs: none. Complete remote branch inventory: `main` = `b0a6d7e1552d0a28f6abc30978cc25b7da3a8461`; `task/adopt-01` = `5276f166a594b7cdf91733f80b8e87452c4c6224`. Primary checkout clean and fast-forwarded; task worktree retained.
- [Main CI 36334763241](https://github.com/ArcForges/Web/actions/runs/36334763241) succeeded: source Linux/Windows, audit, both CodeQL jobs, Build static candidate, Verify and Deploy Cloudflare. Main dependency review was correctly skipped.
- GitHub Releases / Cloudflare latest candidate: [web-0.1.0-ci.62.1](https://github.com/ArcForges/Web/releases/tag/web-0.1.0-ci.62.1), release ID `397730908`, published 2026-09-27T16:53:06Z, targeting frozen main. The private Web workspace is not an npm library publication; its registry scope here is the site/Worker candidate and Cloudflare receipt.
- Candidate asset `web-0.1.0-ci.62.1.tar.gz`: ID `593343734`, metadata size `392300`, digest `sha256:29e473949343676f9621d1a8061a076ee2969a1b01f2dd145e8a00f919ef0375`.
- Provider receipt asset `deployment.json`: ID `593343735`, metadata size `212`, digest `sha256:3a45228eac8af143c132ac0796a7380986a50993c90f2da9ea937b1996a5fc5e`.
- [Deployment job](https://github.com/ArcForges/Web/actions/runs/36334763241/job/108663627159) confirms upload of `arcforges-web` with provider version `4f9bd451-88de-483b-95a9-a95cf1846ea2`. Original receipt also retained as [action artifact 10936629029](https://github.com/ArcForges/Web/actions/runs/36334763241/artifacts/10936629029), named `cloudflare-evidence-36334763241-1`.
- Evidence observed 2026-09-27 after publication. Only metadata and original CI/provider logs were inspected; no published bytes, local product build, browser/runtime test or live-service probe. Deployment success is not product acceptance.

## Interpretation and next work

Open PR and remote-branch inventories are snapshots taken after each instruction PR merged. Retained `task/adopt-01` branches preserve the reviewed inputs; their existence is not unfinished implementation. Later work must cite these frozen heads and separately record any relevant post-baseline changes.

All adoption slices begin from this common baseline once this record is reviewed and merged. Their per-task classifications, exact bound source scopes, inherited evidence, adjustments and conflicts belong in their own ledger records. This record makes no source-cleanup or downstream acceptance claim.

