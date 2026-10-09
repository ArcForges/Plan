---
task: WEB.40
status: delivered
recorded: 2026-10-09
claimant: w-deku-20261008-web-40
epoch: 1
---

# Blazor migration of the existing Web (C# Site, Blazor WebAssembly profiles, C# policy)

## Evidence

- Implementation: Web [PR #35](https://github.com/ArcForges/Web/pull/35), "[WEB.40] Blazor WebAssembly migration of Web", was reviewed and merged at head `c58e5280f0d54c2c754c1806e41de23360526e45` as `c8588681da0c25784ab6d6d82165e2903bd62764` on `main`, with `--merge --match-head-commit`, at 2026-10-09T14:33:01Z. The integration role `integration:Web` was held by `w-deku-20261008-coord` (coordinator-verified; not in the PR text).
- Review trail (PR #35 comments):
  - The independent reviewer session `w-deku-20261008-rev-web-40` authored none of the change. Every session and the PR author ran under one GitHub account (`deku2026`), and the approvals are PR comments posted by the coordinator under the publication protocol, not GitHub review events. Independence is by session only.
  - Round 1 at `58f44c4` had one material finding: the nuspec digest convention in the admission records. It was fixed in `6ff8e1e` by successor receipt `web-40-admission-r14`, a restored-nuspec comparison in the policy test, and a `.gitleaks.toml` path widening. Round 2 approved `6ff8e1e` (full head `6ff8e1eef7412a468431b958087bb7b08ee35160`).
  - Delta approvals followed for `efe787254ae64cc8027a6b801b3cbd9080481321` (including a named exact-head review of the `.gitleaks.toml` change), `4cca32e4157c97953fd33cafc8022bb4a9b07a62` (coordinator decision S20(a)), and the final head `c58e5280f0d54c2c754c1806e41de23360526e45`.
  - Two approved heads, `6ff8e1e` and `4cca32e`, had hosted failures after their approval comments. Each was fixed in a later head that was reviewed.
- Hosted failures and root causes (run logs read with `gh run view --log-failed` and grep; no secret values read or printed):
  - Run 37902336261 at `6ff8e1ee` (failed):
    - Source (ubuntu-latest): `csharp-candidate.test.ts` failed because the test built a local identity while `GITHUB_ACTIONS=true`. Fixed in `efe7872`: the test reads the identity with the `GITHUB_*` variables cleared; the production assertion is unchanged.
    - C# restore, build, test and publish (windows-latest): `NuGetClosureAdmissionTests` failed because the hosted Windows image preinstalls the wasm-tools workload, so no NuGet copy of the browser-wasm runtime pack is restored. Fixed in `efe7872` with an explicit per-OS packs-folder table (a Windows row requiring the content marker `runtimes/browser-wasm/native/dotnet.native.wasm`, and a Linux row), with empty-folder and partial-folder negative controls.
    - Dependency audit and repository checks: gitleaks reported one `generic-api-key` finding at `eng/contracts/ArcForges.Contracts.PublicApi/1.0.0-ci.287.1/source.json` line 9, the SHA-256 of the packaged native-auth schema. Fixed in `efe7872` by a path-, rule- and line-bound allowlist; receipt `web-40-admission-r15` records the exception.
    - Verify: failed downstream of the jobs above.
  - Run 37936152252 at `4cca32e4` (failed):
    - Dependency audit and repository checks: actionlint SC2012 (`ls`) at `.github/workflows/ci.yml:408`, the main-push Site archive step. Fixed in `c58e528` with a nullglob array, a one-archive requirement and a name-equals-digest check; receipt `web-40-admission-r17` records the change.
    - Verify: failed downstream.
- CI receipt:
  - Main-push CI run [37945013754](https://github.com/ArcForges/Web/actions/runs/37945013754) on `c8588681` completed with conclusion success. Every job passed: Dependency audit and repository checks; C# restore, build, test and publish on windows-latest and ubuntu-latest; Source on both; CodeQL (javascript-typescript, actions, csharp); Build and verify the C# static candidate and profile bundle; Verify; Deploy Cloudflare. Dependency review was skipped on push.
  - The PR gate at the final head `c58e528` is run [37938553253](https://github.com/ArcForges/Web/actions/runs/37938553253): 12 checks passed, and Deploy Cloudflare was skipped on pull_request.
  - Deploy Cloudflare job 113871267616 logged `Candidate verified: 0.1.0-ci.111.1 c8588681da0c25784ab6d6d82165e2903bd62764 (20 members)` and `Current Version ID: e8f8cc7c-d0f7-4a84-966b-2f172c59d40d`. It also logged `No targets deployed for arcforges-web`. That line is the baseline behaviour (workers_dev false); the previous main-push deploy, run 37729949245 on 2026-10-08, logged the same line. The `digest-mismatch: error` text in the download-artifact step is the action's default input echo, not a failure.
- Prerelease `web-0.1.0-ci.111.1` (target `c8588681`) has four assets, read with `gh release view`: `deployment.json` (213 bytes), `web-0.1.0-ci.111.1.tar.gz` (29949), `web-profiles-4afc8f285a7a64202ce221bc4e3011a9f8b6de641d50eef0a537677e80eaef9a.tar` (18636800) and `web-site-573575617dec11d2d3678bf5ccd92728190b64a79e7907e050764fd8a1d131ac.tar` (26112). Nothing was downloaded.
- Port table, `docs/web-40-react-retirement.md` at `c58e528`. It maps each retired test to a successor. Most rows are ported (Account and Chat session, CSRF and route cases in `tests/ArcForges.Web.App.Tests`; bUnit focus order; archive, rule and build refusal cases in `tests/ArcForges.Web.Tooling.Tests`; the naming scanner and architecture policy in `tests/ArcForges.Web.Policy.Tests`; the contract and Site cases in `tests/ArcForges.Web.Site.Tests`). Three rows are not complete (see Gaps 2).
- Byte comparison of the public page inventory, `docs/web-40-site-parity.md` (recorded at source `80900a1`, before the React sources were removed):
  - Element skeleton, text and metadata equal for `/`, `/hello/` and `/cloud-hello/`.
  - `404.html`, `404.css`, `robots.txt` and `favicon.svg` byte identical; stylesheet content byte identical (8973 bytes; the content-hashed name differs).
  - `_headers` identical except the CSP `script-src`, which is an accepted TB-01 difference.
  - The HTML pages are not byte identical, and the doc says byte parity is not shown. Brief section 10, "WEB.40 parity, focus and accessibility re-proof", waives byte parity and makes normalised-DOM parity the gate (see Gaps 3).
- NuGet closure receipts: `eng/policy/dependency-reviews/web-40-admission-r1.json` through `web-40-admission-r17.json`, a successor chain in which each receipt on the active path names the reviewer. `r17` supersedes `r16` and differs from it only in the `ci.yml` input hash (`45457067...`, equal to the committed file's sha256) and in its links and rationale. The reviewer's `c58e528` comment records that 71 of 71 `nuspecSha256` rows equal the restored `.nuspec` bytes, that `contentHash` equals the lock and `.nupkg.metadata` values for 69 lock rows, and that `licence-evaluated` passed. I did not re-run those checks. The r14 rationale sentence was corrected by r15 and r17; committed receipts are not rewritten.
- Validation clauses checked against the Web worktree and hosted runs:
  - Account and Chat profile tests for session, CSRF, exact-value and typed-failure semantics are in `tests/ArcForges.Web.App.Tests` and ran in the hosted C# jobs at `c58e528`.
  - The forbidden-term scanner runs in the policy suite (`tests/ArcForges.Web.Policy.Tests/NamingScannerTests.cs`). CI runs that suite in its Test step (`.github/workflows/ci.yml`, comment at line 128), so it is a failing check in Web's own PR build (WP-05.02).
  - CI builds and tests the explicit `CSHARP_PROJECTS` list (`ci.yml` lines 22-26), which covers every `win.slnx` project except `tests/browser`. `win.slnx` itself is an optional solution (`docs/validation.md` line 13).
  - The Operations skeleton's CSP token-set assertion is in `tests/ArcForges.Web.Operations.Tests/OperationsProfileTests.cs`; I confirmed the file contains it by grep, and the hosted C# jobs ran it.
  - `.github/dependabot.yml` has a nuget entry and retargeted npm groups for wrangler and `@cloudflare/*`. I did not check each group against the record.
  - `.gitleaks.toml` has two `[[allowlists]]` blocks, each bound to a path, the `generic-api-key` rule and specific lines. The native-auth block was added in `efe7872`. Its exact-head review and the retained CI runs (`efe7872` and `c58e528`) are recorded. Its named authority is not located (see Gaps 5).

## Scope (2026-10-09)

Under the user's scope correction of 2026-10-09 (planning repair P2-026, merged on Plan `main` at `2ecd6ef8`; brief section 0a), WEB.40 was finished as the C# migration of Web, with the reductions and additions below. Each is cited by its brief section 10 or 11 item.

- **S17(a), brief section 11 (Node build tooling): out of scope, not completed.** The remaining Node TypeScript build, policy and provenance tooling port is out of scope. It covers `dependency-policy.ts`, `provenance.ts`, `licence-boundary.ts`, `project.ts`, `build-identity.ts`, `cloudflare.ts` and `candidate.ts`; the node:test provenance tests `build-identity`, `legal-path`, `source`, `csharp-candidate`, `lock-provenance` and `cloudflare-delivery`; and the xUnit successor for every provenance test. Node stays for wrangler and these build tools. Product and business code is C# (Blazor), and the Worker stays a thin adapter. The outcome and validation clauses that name that port are carved out, not completed. `tests/provenance` is retained unchanged.
- **S17(b), brief section 11 (ADP-07 bindings):** 19 changed paths outside the WEB.40 writes are accepted as supporting-file bindings recorded in PR #35: `global.json`, `Directory.Build.props`, `.editorconfig`, the vendored `eng/naming` tool, the `eng/contracts` PublicApi copy, `eng/version-sources.json`, the root `README.md`, `AGENTS.md`, `CONTRIBUTING.md` and `THIRD_PARTY_NOTICES.md`, and the deleted React, Prettier, VS Code and Playwright configurations.
- **S17(c) and (d), brief section 11:** the r14 rationale is corrected by a successor, and the accessibility refinements (the 2.5.8 spacing exception, the skip-link item, and committing or hashing the axe report) are a non-blocking follow-up. WEB.40 has no streaming surface; PRF.11 owns the streaming proof.
- **S20(a), brief section 11 (WEB.40 before merge):** a deterministic `web-site-<sha256>.tar` built with the existing ustar writer, released on main-push only, and the root `index.html.br` and `index.html.gz` excluded from the profile bundle. It was one delta commit on PR #35 (`4cca32e`), hardened in `c58e528`. The base href stays "/" (D1).
- **Brief section 10, "WEB.40 Site interactivity and formatting":** `/hello/` and `/cloud-hello/` keep their static text, and their live greeting and connection controls are retired (no runtime JavaScript, TB-01). No Blazor route is added to the Site, and `ArcForges.Web.App` is the only interactive browser application. The formatting gate is `dotnet format --verify-no-changes`; Prettier and Biome are retired.
- **Brief section 10, "WEB.40 parity, focus and accessibility re-proof":** byte parity is waived for a normalised-DOM gate. Chat Cancel uses focus option (a). The accessibility re-proof of the 14 screen states is in `docs/web-40-accessibility.md`.
- **Operations profile:** a skeleton only (`src/ArcForges.Web.Operations` and its skeleton tests). OPS.05 builds the operator features.
- **GOV.11 policy suite:** outcome item (7) and the P2-026 review fix carve it out of the record. PR #35 nevertheless ports it as `tests/ArcForges.Web.Policy.Tests` (108 tests, per the reviewer). That port is not counted as delivered scope of this record.
- **Not in scope:** the Blazor proof structural gates and interaction budgets (PRF.11), the streaming proof (PRF.11), the OPS.11 package-review routes (P2-026), and macOS (P2-023).

## Gaps against the status rule

Status is "delivered" because the record's evidence and validation are not all met by real evidence. Each gap is named.

1. **CLOUD.71 bundle-naming coordination note: not met.** `docs/profile-bundle.md` ("CLOUD.71 and CLOUD.85 coordination") says the note is pending and not claimed. I found no recorded note in `Plan/ledger/tasks/` (the existing `cloud-71.md` record concerns the earlier `web-0.1.0-ci.90.1` bundle from PR #30), in the Design lane `cloud.md`, or in the Design decisions.
2. **Port table: not complete.**
   - The `tests/unit/app-proof.test.ts` row is "Remaining": the Blazor proof structural gates and the interaction budgets stay with PRF.11.
   - `tests/browser/cloud-hello-fixture.spec.ts` has no successor. It is retired with the hydration decision in brief section 10, "WEB.40 Site interactivity and formatting", and not ported.
   - The `tests/unit/app-routes.test.tsx` row says Cancel in Chat is "still open (decision 8)", but decision 8 in the same document records option (a) as resolved. The row needs correcting.
3. **Byte comparison of the public page inventory: not met literally.** The HTML pages are not byte identical, and no byte comparison passed. The only waiver is the coordinator's adjudication in brief section 10, "WEB.40 parity, focus and accessibility re-proof", which substitutes normalised-DOM parity. That gate requires the CSP to be equal except for listed intended differences, and the recorded CSP differs (`script-src 'self'` against seven hashes). The difference is listed as accepted (TB-01). `docs/web-40-site-parity.md` still says no waiver is recorded in that file, so the document is stale against the brief.
4. **Rollback acceptance named gate (outcome item 5): not located.** Brief section 10 and the outcome require a local operator run receipt. None is in the Web worktree. `docs/deploying.md` describes the rollback procedure but records no run.
5. **Gitleaks exception named authority: not located.** The validation clause requires named authority for any `generic-api-key` exception change. I did not find it in the brief, the PR body or the PR comments. The exact-head review and the retained CI runs are present.
6. **Validation clauses without a located receipt.** The Linux-affected checks in WSL2 Debian have no receipt in the PR. The PR records only that the WSL2 restore is unlocked. The local browser suites beyond the recorded runs have no receipt at the merged head (see the Untested coverage section).
7. **Browser E2E (Microsoft.Playwright for .NET):** local opt-in only, not run in CI, with no hosted browser (P2-017). The recorded local runs are in the Untested coverage section.

## Untested coverage (stated expressly)

- **Browser suites (local opt-in, never CI):** `LocalSiteBrowserTests`, `LocalBuildIdentityBrowserTests`, `LocalFocusBrowserTests` and `LocalAccessibilityBrowserTests` in `tests/browser/ArcForges.Web.Browser.Tests`. Recorded runs: the accessibility run at `73173c2` (10 passed; the Chrome build used is not recorded), and the focus run on the recording machine (2 passed, on the installed Chrome). The Site and build-identity browser runs are not recorded at the merged head `c58e528`. No browser run is hosted.
- **Live checks:** no live check of the Web public site, the Account profile or the Chat profile on any origin. The proof-origin serving (CLOUD.85) is not run. The main-push deploy logged the candidate as verified and `No targets deployed` (the baseline). That is not a live-version check, and the rollback acceptance gate is not run (Gap 4).
- **Accessibility:** the human assistive-technology session and the judgement items (rows marked "not verified: needs a human assistive-technology session") are open and not claimed. axe covers only part of WCAG 2.2.
- **Profile budgets:** CI enforces the measured budgets. The interaction ceilings are re-baseline-pending under PRF.11.
- **Checks I did not run:**
  - gitleaks (hosted only; one hosted run found one leak, fixed in `efe7872`);
  - the Node 24.21 pin gate (local Node is 24.20; the reviewer stubbed only the pin assertion locally, and the hosted Source job ran it at `c58e528`);
  - the Linux checks in WSL2 (Gap 6);
  - the NuGet row checks (reviewer-verified; I did not re-run them).
- **Reproducibility:** the profile bundle is reproducible within one build only. Razor-generated sources embed the checkout path, so the bundle differs across separate checkouts. `docs/profile-bundle.md` says "deterministic" and should read "within one build" (review non-blocking). No cross-checkout reproducibility is claimed.
- **Operations and streaming:** the Operations profile is a skeleton, and no operator feature is tested. WEB.40 has no streaming surface, and PRF.11 owns the streaming proof.
- **Dependabot:** no open Dependabot pull request was touched, and none was run.
- **Retired tests without successors:** `tests/browser/cloud-hello-fixture.spec.ts` (Gap 2), retired by the brief section 10 adjudication and not tested by any successor.
