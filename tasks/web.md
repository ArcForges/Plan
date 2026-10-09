# ArcForges delivery task prompts — Web

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Web

```text
Execute ArcForges delivery task WEB.01 — C# static Site generator (Razor HtmlRenderer) and determinism engine.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-01 (python tools/delivery.py claim WEB.01 --worker <name>); task branch task/web-01 in Web; ledger record ledger/tasks/web-01.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: The C# static Site generator (ArcForges.Web.Site, first-party Razor HtmlRenderer, build time, with no WebAssembly or runtime JavaScript on public pages per TB-01) generates the full public locale/URL inventory, documentation versions, sitemap, metadata and redirects, deterministically, with no Account/Chat profile bundle or private config leaking into the static output.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.00

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.40: C# static Site generator and migrated public page inventory (WEB.40 parity port)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.Site/**; Web:.gitleaks.toml (only exact path-and-digest generic-api-key exceptions re-derived for the C# static output, each change under the WEB.40 successor policy and the GOV.11 review standard); Web:tests/ArcForges.Web.Site.Tests/** (incl. the xUnit successor of tests/provenance/candidate.test.ts: Gitleaks exception-boundary positive and negative tests)
Shared resources (follow the owner protocol): RES-contract-consumer-pins (append): A consumer task updates the pin it needs through a reviewed dependency change to the exact published candidate containing its closure; no consumer pins an unpublished closure or references Contracts source.
Unblocks: OPS.04, WEB.02, WEB.03, WEB.04, WEB.05, WEB.06, WEB.07

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Two full builds with identical inputs compared byte-for-byte; no-script navigation/content tests (xUnit over parsed HTML); single-content-change diff; build with network disabled after an approved NuGet restore (CI-eligible offline checks). Keep the pinned Gitleaks scan enabled. Its generic-api-key exception may match only an exact path-and-digest pair enumerated for the C# static output (each bound on the same line, AND). The enumerated set is not assumed: it is established only by observing the C# output and freezing the observed set by a reviewed change under the WEB.40 successor policy. The Web r8 counts (eight lines, six unique values) are not carried over as verified facts for the C# output. Until the reviewed set is frozen the scan fails closed on any generic-api-key match, and any later count outside the frozen set fails the scan. Freezing or changing the set is a security-exception change and needs the GOV.11 review standard (named authority, independent exact-head review and retained CI before merge). The xUnit policy tests must test the actual config and profile bindings with positive and negative cases for a changed digest, another path, an unrelated 64-hex value and credential-looking text. No generic 64-hex patterns, whole-file or commit suppressions, scanner/workflow/rule-algorithm changes, candidate-generation algorithm changes or new dependencies: the only dependency admission is the WEB.40 NuGet closure, which needs the same GOV.11 review standard (independent exact-head review and retained CI before merge).
Completion evidence for the ledger: Determinism comparison and diff-minimality results; pinned Gitleaks results on the C# static output, with the observed generic-api-key line count and unique path-and-digest values recorded as to-be-observed evidence (not assumed from the r8 counts), the frozen exception set with its reviewed record reference, and negative path/digest-boundary evidence.
Notes: Its only real start need (WP00/WP02) is already satisfied; the current serial plan defers WP47 until after WP40, but nothing blocks starting this immediately. The candidate provenance test reads the actual .gitleaks.toml and browser-resources-r8.json, verifies the six unique exact path/digest bindings for the eight observed findings, and rejects changed-digest, different-path, unrelated-64-hex and credential-text cases; it must not alter candidate generation. Planning repair 2026-10-08 (DLV-34; P2-021): React Router build-time prerendering becomes the C# HtmlRenderer generator in src/ArcForges.Web.Site (apps/site retires after the WEB.40 parity port) per P2-021 item 2. Determinism, locale/URL inventory, the no-leak rule and the exact-exception discipline are kept. The Gitleaks generic-api-key exception set is fail-closed until observed on the C# output and frozen by a reviewed change; the r8 counts are an assumption for the C# output, not a verified fact, and are not used as the bound. Freezing or changing the set is a security-exception change under the GOV.11 review standard (named authority, independent exact-head review, retained CI). The one-for-one xUnit successor of tests/provenance/candidate.test.ts is listed in writes. Starts only after WEB.40 delivers. Planning repair 2026-10-09 (P2-026; scope correction): the GOV.11 start is removed because GOV.11 is out; the GOV.03 Node/npm start is removed because its pins are replaced by the .NET build governance of WEB.40, which this task already starts on.
```

```text
Execute ArcForges delivery task WEB.02 — Versioned public content and pricing inputs (catalogue.json).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-02 (python tools/delivery.py claim WEB.02 --worker <name>); task branch task/web-02 in Web; ledger record ledger/tasks/web-02.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Catalogue, release metadata, changelog and legal versions are consumed from declared versioned local inputs with no live provider fetch during build; the pricing projection shows its effective version/time.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.01

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.01: static generator
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.Site/content/**; Web:src/ArcForges.Web.Site/catalogue.json
Unblocks: WEB.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Hard-coded-version/price scan; comparison of public projection to the selected approved snapshot — offline
Completion evidence for the ledger: No independently hard-coded product version/private supplier price
Notes: Private candidate builds may use named test-only offer/release fixtures per WP-47.01; the real WP42/44 numeric join for public promotion is explicitly deferred to WP50, not required to close this task's own gate. Planning repair 2026-10-08 (DLV-34; P2-021): The versioned catalogue and pricing data files are kept as data. Their loader moves from the React/Vite import to typed C# configuration. No live provider fetch during build, unchanged. Writes move to the C# site project. Planning repair 2026-10-09 (P2-026; scope correction): reduced: catalogue, pricing, release, changelog and legal rows for ArcSlate and ArcNotes, and the macOS download, signing, notarisation and Apple store rows, are out of scope, not completed.
```

```text
Execute ArcForges delivery task WEB.03 — Rendering and performance.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-03 (python tools/delivery.py claim WEB.03 --worker <name>); task branch task/web-03 in Web; ledger record ledger/tasks/web-03.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Above-the-fold content ships in the HTML delivered by the C# static generator, so no JavaScript is needed to render public pages (TB-01). Assets are content-hashed with short-lived HTML caching, no blocked third-party resource sits on the critical path, and the p75 LCP/INP/CLS budgets (AL-05) are met.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.02

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.01: static generator
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.Site/**; Web:tools/ArcForges.Web.Tooling/**
Shared resources (follow the owner protocol): RES-web-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: WEB.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): No-script render test; critical-path resource audit; p75 performance measurement; global-reachability check on every third-party host — offline/lab Public-Site CSP assertion (xUnit over the generated headers and meta tags, P2-021 item 2): the static public pages carry exactly the strict token set script-src 'self' with no unsafe-eval, unsafe-inline or wasm-unsafe-eval token, style-src 'self', and no script element or Blazor _framework reference on any public route.
Completion evidence for the ledger: No-script render, critical-path audit and performance measurements
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Public pages stay static HTML and CSS before JavaScript runs (TB-01 is a live rule). The generator emits no WebAssembly or _framework script on public routes. The React tooling/** scripts port to C# under tools/ArcForges.Web.Tooling. The AL-05 public budgets are not re-baselined. Planning repair 2026-10-08 (DLV-34; P2-021 item 2): The strict public-Site CSP token set (no wasm-unsafe-eval) is asserted in validation; the App profiles keep their own token set under WEB.16.
```

```text
Execute ArcForges delivery task WEB.04 — Internationalisation.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-04 (python tools/delivery.py claim WEB.04 --worker <name>); task branch task/web-04 in Web; ledger record ledger/tasks/web-04.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Locale-scoped URLs with alternate-language annotations, no client-only switching and no trapping redirect; every user-visible string, including generated pages, is localisable through .NET localisation resources (.resx) with the same criteria as before.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.03

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.01: static generator
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.Site/**
Unblocks: WEB.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Locale routing/annotation tests, no-trap assertion, pseudo-localisation pass — offline
Completion evidence for the ledger: Locale routing, no-trap and pseudo-localisation results
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): The mechanism moves from React i18n to .NET localisation (.resx) under the C# static generator. The locale routing, no-trap and pseudo-localisation criteria are unchanged.
```

```text
Execute ArcForges delivery task WEB.05 — Documentation, downloads and legal surfaces.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-05 (python tools/delivery.py claim WEB.05 --worker <name>); task branch task/web-05 in Web; ledger record ledger/tasks/web-05.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Versioned per-product documentation, a no-account-gate download surface serving signed artifacts with published hashes, an update feed surface, and versioned legal pages with effective dates.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.04

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.01: static generator
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.Site/content/**; Web:src/ArcForges.Web.Site/Pages/**
Unblocks: WEB.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Documentation version routing; download integrity verification against published hashes; no-account-gate assertion; legal version-history tests — offline against labelled fixtures
Completion evidence for the ledger: Download integrity, no-gate and legal versioning results
Notes: Private candidate download fixtures are labelled; public promotion with real signed Desktop/Android artifacts is joined at WP50, not required to close this task. Planning repair 2026-10-08 (DLV-34; P2-021): Versioned docs, downloads and legal pages become generated surfaces of the C# static generator. The download-integrity, no-gate and legal-versioning criteria are unchanged. Legal version-history tests run as xUnit tests against labelled fixtures. Planning repair 2026-10-09 (P2-026; scope correction): reduced: per-product documentation and download rows for ArcSlate and ArcNotes, the macOS and Apple store download rows, and any Play store download route are out of scope, not completed. The Android download is the direct APK channel only (S11).
```

```text
Execute ArcForges delivery task WEB.06 — Accessibility and analytics.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-06 (python tools/delivery.py claim WEB.06 --worker <name>); task branch task/web-06 in Web; ledger record ledger/tasks/web-06.md.
Kind/size: feature/S. Baseline: not-started.
Outcome: Accessibility semantics and keyboard-only navigation on every page; minimal privacy-preserving analytics with no cross-site identifier and no consent wall.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.05

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.01: static generator
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.Site/**; Web:tests/ArcForges.Web.Site.Tests/**
Unblocks: WEB.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): CI-gated (offline) accessibility semantics in xUnit/bUnit over the generated static pages and rendered components: roles, accessible names, labels, focus order, live regions, landmarks, alt text, heading order, lang, focus-visible styles and keyboard-reachable controls; axe-core is local opt-in test-only tooling run through Microsoft.Playwright for .NET, injected only into the page under test and never shipped (browser E2E is never CI: playwright.config.ts CI guard, P2-017), plus a dated manual verification; analytics payload audit (xUnit, offline).
Completion evidence for the ledger: Offline xUnit/bUnit accessibility semantic results on the generated pages and components; local axe-core opt-in results; dated manual record; analytics payload audit with no cross-site identifier.
Notes: Planning repair 2026-10-08 (DLV-34; P2-021, P2-017; section 6 decision 3): Accessibility semantics and keyboard navigation are checked on the C# generated pages and components. The CI gate is the offline xUnit/bUnit semantic assertion set (roles, names, labels, focus order, live regions) in validation. axe-core is local opt-in test-only tooling run through Microsoft.Playwright for .NET, injected only into the page under test and never shipped. Baseline fact: axe-core tests already run only in tests/browser under the Playwright CI guard, so no CI-gated axe check is removed by this repair. The criteria are unchanged. Planning repair 2026-10-09 (P2-026; scope correction): no part of this task is out of scope: minimal privacy-preserving analytics and the analytics payload audit stay in scope (PV-05; S12).
```

```text
Execute ArcForges delivery task WEB.07 — Independence and atomic deployment.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-07 (python tools/delivery.py claim WEB.07 --worker <name>); task branch task/web-07 in Web; ledger record ledger/tasks/web-07.md.
Kind/size: release/S. Baseline: not-started.
Outcome: The site remains fully available during a full Cloud outage, deploys atomically per surface from a promoted artifact (static C# output on Cloudflare Static Assets, no production Node server), and rollback restores the previous artifact set. The Cloudflare worker/index.js stays a thin platform adapter with no business rule.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.06

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.01: static generator
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:wrangler.json; Web:worker/**; Web:.github/workflows/ci.yml; Web:tools/ArcForges.Web.Tooling/Cloudflare/**
Shared resources (follow the owner protocol): RES-web-app-routing (append): The application shell task owns root route registration; each surface adds its own route module and per-origin edge directory.; RES-web-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: WEB.09, WEB.30, WEB.31

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Cloud-outage independence, atomic-deployment and rollback tests: the offline checks (CI-eligible) exercise the deployment adapter against recorded Cloudflare API fixtures and a local wrangler dry-run, and compare the promoted artifact byte-for-byte with the build output. The live-account promotion and rollback check is a local opt-in run by an operator against the real Cloudflare account, recorded as an operator run receipt, not a hosted live-service CI check (P2-017); no live-service CI job is added. The existing main-push Cloudflare deploy job in .github/workflows/ci.yml is a deployment step outside validation and stays (section 6 decision 2); it is not counted as validation evidence. Rollback acceptance is a named gate (PG-23, REL.05) recorded by the local operator run receipt.
Completion evidence for the ledger: A full cloud outage leaves the site fully available; deployment is atomic; rollback restores the previous set. Rollback acceptance is the named gate evidence (PG-23, REL.05) recorded by a local opt-in operator run receipt, not a CI job (P2-017; section 6 decision 2).
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Stays a thin-adapter task (P2-021 item 1). The Node/TypeScript tooling/cloudflare.ts deployment script ports to C# under tools/ArcForges.Web.Tooling. Node remains wrangler build/deploy tooling only.
```

```text
Execute ArcForges delivery task WEB.08 — Owned consumer design system (Razor class library ArcForges.Web.Ui).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-08 (python tools/delivery.py claim WEB.08 --worker <name>); task branch task/web-08 in Web; ledger record ledger/tasks/web-08.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: src/ArcForges.Web.Ui (the Razor class library that replaces packages/ui) grows from a placeholder Shell/Button into a full design-token system (typography, spacing, colour, themes), owned accessible Blazor components, a test-only component catalogue, approved visual baselines and reusable account/usage/chat primitives, with localization/long-label/mobile-nav/focus/reduced-motion/loading-error-empty variants.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.07 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.07

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.40: the migrated Web repository baseline (Razor component port of the placeholder Shell/Button)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.Ui/**; Web:tests/ArcForges.Web.Ui.Tests/**
Shared resources (follow the owner protocol): RES-web-shared-ui (append): The design-system task owns the shared UI package; surfaces request components through it; additions after it are additive.
Unblocks: WEB.09, WEB.10, WEB.19

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): bUnit component behaviour tests, including the CI-gated accessibility semantic assertions of WEB.06 on every component state; production-rendered Microsoft.Playwright for .NET visual snapshots for representative viewport/theme/locale combinations (local opt-in, per the Playwright CI guard); axe-core on the same states as local opt-in only, injected only into the page under test; dated human visual/keyboard review; NuGet licence and provenance checks.
Completion evidence for the ledger: Approved consumer layouts and complete accessible states
Notes: Has NO dependency on WEB.01-WEB.07 (different package, only needs WP02 which is already satisfied) and should be started in parallel with the site generator work, not after it — it is the critical-path input for both WEB.10 (account) and WEB.19 (chat). Planning repair 2026-10-08 (DLV-34; P2-021): packages/ui (React Shell/Button and 373 CSS lines) becomes the Razor class library ArcForges.Web.Ui. The token system, catalogue, visual baselines and variants are kept. Still no dependency on WEB.01-WEB.07, and it is still the critical-path input for WEB.10 and WEB.19. Planning repair 2026-10-09 (P2-026; scope correction): the GOV.03 Node/npm start is removed (S10); the .NET build governance comes from the WEB.40 start.
```

```text
Execute ArcForges delivery task WEB.09 — Verify the owned Site artifact and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-09 (python tools/delivery.py claim WEB.09 --worker <name>); task branch task/web-09 in Web; ledger record ledger/tasks/web-09.md.
Kind/size: integration/S. Baseline: not-started.
Outcome: The C#-generated static Site with localization/SEO and no production Node server or runtime JavaScript is verified end to end; independently published product/version/download metadata is consumed through the fixed release contract, with pending later owners and their closing gates recorded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.90
- WP-47:browser-matrix-acceptance-paragraph-brow Browser matrix acceptance paragraph (browser-support.v1 for the static site output) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md, package-level obligation

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.02: content/pricing inputs
- [artifact] WEB.03: performance
- [artifact] WEB.04: i18n
- [artifact] WEB.05: docs/downloads/legal
- [artifact] WEB.06: a11y/analytics
- [artifact] WEB.07: deployment
- [artifact] WEB.08: design system
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.Site/**
Unblocks: REL.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Static, no-script, public-Site CSP token-set (WEB.03), localization, link and artifact-version checks (xUnit); accessibility through the CI-gated WEB.06 xUnit semantic checks, with axe-core only as local Microsoft.Playwright for .NET opt-in for browser rendering, injected only into the page under test; private candidate download fixtures labelled; public promotion waits for WP50.
Completion evidence for the ledger: Owned-artifact-and-real-integration receipt including browser-support.v1 evidence for the site output
Notes: Provides the tooling WP45's operations console needs ("47 tooling must precede 45" per producer-artifacts-and-integration.md); the commerce, policy and operations lanes should reference this task's 'web-static-generator'/'web-design-system' tokens as its own start need rather than waiting on all of WP47's numeral position in the old serial plan. Planning repair 2026-10-08 (DLV-34; P2-021): Verifies the C# generated Site artifact instead of the React build. The no-script, localization and release-contract criteria are unchanged.
```

```text
Execute ArcForges delivery task WEB.10 — Account Blazor shell: route graph, deployment-profile selection, generated C# SDK wiring.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-10 (python tools/delivery.py claim WEB.10 --worker <name>); task branch task/web-10 in Web; ledger record ledger/tasks/web-10.md.
Kind/size: producer/XL. Baseline: not-started.
Outcome: The ArcForges.Web.App Blazor WebAssembly project is created with the account deployment profile (standalone, RunAOTCompilation=false by default): route graph and shell composed from ArcForges.Web.Ui and the generated C# gRPC-Web client (Grpc.Net.Client.Web, binary framing); Android callback/assetlinks wiring; responsive overview/navigation; safe public runtime config; error boundaries; and loading/empty/pending/expired states with cache-clear-and-abort on user/workspace change (in-memory state only, no persistent account cache).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.00

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.08: design system tokens/components
- [contract] CON.07: generated C# gRPC-Web client from the published Contracts NuGet candidate, at the current release covering the account and chat wire surface (precondition: the NuGet identity is verified at start from the CON.07 publication record)
- [artifact] WEB.40: the migrated Blazor WebAssembly project baseline and C# NuGet closure
- [artifact] PRF.11: Blazor WebAssembly production proof (real AOT probe, CSP, exact values, binary streaming decision)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.12: identity/browser/native endpoints

Permitted write scope: Web:src/ArcForges.Web.App/**; Web:tests/ArcForges.Web.App.Tests/**; Web:win.slnx (register the profile projects only); Web:Directory.Packages.props (NuGet pins needed by the shell only)
Shared resources (follow the owner protocol): RES-contract-consumer-pins (append): A consumer task updates the pin it needs through a reviewed dependency change to the exact published candidate containing its closure; no consumer pins an unpublished closure or references Contracts source.; RES-web-app-routing (append): The application shell task owns root route registration; each surface adds its own route module and per-origin edge directory.; RES-web-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-web-shared-ui (append): The design-system task owns the shared UI package; surfaces request components through it; additions after it are additive.
Unblocks: WEB.11, WEB.13, WEB.14, WEB.15, WEB.16, WEB.19

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): xUnit state/route tests and bUnit component tests (no-cookie-leakage, state, PKCE and origin-mismatch, Android-verified-links tests); production profile/chunk isolation, both themes, keyboard and narrow layouts (fixture-backed CI plus local opt-in real-browser evidence).
Completion evidence for the ledger: Profile isolation and composition results
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): The apps/app workspace registration moves to the Blazor project. The chain of cookie/PKCE/origin/cache-clear rules is kept. The shell composes ArcForges.Web.Ui instead of packages/ui. The CON.07 need text names the generated C# client.
```

```text
Execute ArcForges delivery task WEB.11 — Real browser session and step-up acceptance.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-11 (python tools/delivery.py claim WEB.11 --worker <name>); task branch task/web-11 in Web; ledger record ledger/tasks/web-11.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Passkey/email verification/recovery, live opaque cookie session, server-controlled expiry/revocation and sensitive-action step-up work on the real account origin topology; no bearer/refresh token ever enters the app.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.01

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.19: the P2-003 same-origin cookie-session adapter
- [artifact] WEB.10: account shell
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.App/Features/Account/**; Web:tests/ArcForges.Web.App.Tests/**
Unblocks: WEB.12, WEB.18

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Playwright against production assets, edge and real Cloud and D1 is local opt-in (login/logout, two origins and tabs, sibling-origin CSRF, passkey expected origin, replica restart, expiry/revoke races); manual passkey and browser matrix supplements automation; xUnit/bUnit fixture tests for session state, step-up and expiry handling.
Completion evidence for the ledger: Token storage, refresh, step-up and new-browser trust results
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): The passkey WebAuthn call (navigator.credentials) and clipboard/download are the audited JavaScript interop points allowed by P2-021 item 2. No bearer or refresh token enters the app. Session, step-up and expiry criteria are unchanged.
```

```text
Execute ArcForges delivery task WEB.12 — Account and security surfaces.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-12 (python tools/delivery.py claim WEB.12 --worker <name>); task branch task/web-12 in Web; ledger record ledger/tasks/web-12.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Profile, authentication methods, passkey management, sessions, device list with trust/revocation, recovery configuration, API token management (AT-01: personal access tokens with scoped display-once creation and revocation), the sync status view and the security-event view are complete, with step-up required on every sensitive action.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.02

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.11: session/step-up
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.App/Features/Account/**
Unblocks: WEB.17, WEB.18

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Device-revocation-propagation, passkey add/remove, security-event-visibility and step-up-required-per-action tests, API token display-once and revocation tests and sync status view tests — fixture CI plus local opt-in real-Cloud evidence
Completion evidence for the ledger: Device revocation, passkey, step-up, API token and sync status coverage results
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Account and security surfaces are Blazor components in the Account profile. The step-up-per-action and revocation-propagation criteria are unchanged. Planning repair 2026-10-09 (P2-026; scope correction): gains API token management (AT-01) and the sync status view from the requirements/02 section 12 minimum portal scope (S12), which no WEB outcome covered.
```

```text
Execute ArcForges delivery task WEB.13 — Workspace, storage and usage.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-13 (python tools/delivery.py claim WEB.13 --worker <name>); task branch task/web-13 in Web; ledger record ledger/tasks/web-13.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Single-owner workspace settings (no membership/invitation/role/seat surface), service-term/included-capacity display with recovery timing and extra-credit opt-in, storage from committed objects, usage-against-quota with visible reset boundaries, and data-health visibility.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.03

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.10: account shell
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.42: R2/committed-object accounting
- [integration] CLOUD.52: data-health status projection (read-only surface only)

Permitted write scope: Web:src/ArcForges.Web.App/Features/Workspace/**
Unblocks: WEB.17, WEB.18

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Accounting comparison against server-side figures; structural xUnit test over the generated C# operation catalogue and route table asserting no membership, invitation, role or seat operation; projection test asserting no supplier rate or route-weight leakage; capacity-vs-credits never-summed display test.
Completion evidence for the ledger: Storage and usage accounting comparison
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): The no-membership structural test becomes an xUnit assertion over the generated C# operation catalogue and route table, not a TypeScript source check.
```

```text
Execute ArcForges delivery task WEB.14 — Subscription, capacity, credits and hosted checkout.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-14 (python tools/delivery.py claim WEB.14 --worker <name>); task branch task/web-14 in Web; ledger record ledger/tasks/web-14.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Consumer subscription and management views use public server projections and generated C# operations; paid-term state, replenishing capacity and purchased credits display separately; hosted checkout opens in-browser and shows confirming until verified Cloud state changes; no client or provider redirect grants entitlement.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.04 (all work except the parts mapped to WEB.29): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.04

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.10: account shell
- [contract] CON.08: commerce/entitlement wire records
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] COM.14: real commerce ledger/test-mode checkout environment
- [integration] POL.02: real policy projections for rate-limit/recovery reasons

Permitted write scope: Web:src/ArcForges.Web.App/Features/Commerce/**
Unblocks: WEB.17, WEB.18, WEB.29, WEB.30, WEB.31

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Real C# accounting and checkout test-environment flows; exact-amount display using C# decimal and int64/uint64 values end to end (no double or JavaScript Number conversion), correct above the 2^53 JavaScript safe-integer boundary and across the full int64/uint64 range (xUnit/bUnit, offline); duplicate-click, cancelled, failed, late-confirmation, refund, term-expiry and stale-price tests (local opt-in against a real test-mode provider).
Completion evidence for the ledger: Entitlement reason coverage, credit separation and no-payment-field scan
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): The JS safe-integer display boundary is restated as a C# decimal and int64/uint64 boundary (P2-021 item 1 exact-value rule). The acceptance is stronger: the boundary above 2^53 and the full wire range are both tested. Duplicate-click, refund and provider criteria are unchanged.
```

```text
Execute ArcForges delivery task WEB.15 — Data export and deletion.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-15 (python tools/delivery.py claim WEB.15 --worker <name>); task branch task/web-15 in Web; ledger record ledger/tasks/web-15.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Export requests show progress and download; deletion requests show a grace period and an explicit, accurate statement of what is and is not deleted, including that local data is untouched.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.05

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.10: account shell
- [contract] CON.22: published data and export operations
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.45: real export job mechanics

Permitted write scope: Web:src/ArcForges.Web.App/Features/Data/**
Unblocks: WEB.17, WEB.18

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Export-completeness, deletion-statement-accuracy, grace-period and local-data-assertion tests
Completion evidence for the ledger: Export completeness and deletion statement accuracy
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Export progress and download and deletion-statement accuracy are Blazor components calling the generated C# CON.22 operations. Criteria unchanged.
```

```text
Execute ArcForges delivery task WEB.16 — Origin security and performance (account).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-16).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-16 (python tools/delivery.py claim WEB.16 --worker <name>); task branch task/web-16 in Web; ledger record ledger/tasks/web-16.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: A strict CSP on the Blazor WebAssembly profiles: script-src 'self' 'wasm-unsafe-eval' plus only the required framework hashes, never unsafe-eval or unsafe-inline; style-src 'self' with no component that needs inline styles (the exact token set is asserted on the built output; CS-01 is rewritten to it). Per-origin cookie, CORS and CSRF posture, no secret in the bundle, sandboxed preview of user content, and bundle-size and first-interactive budgets re-baselined for Blazor WebAssembly by a reviewed AL-06 record owned by PRF.11, while the regression gate and its 10% regression threshold stay fixed: an AL-06 record may change only the measured baseline values, never the threshold or the gate itself.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.06

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.10: account shell
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:deploy/edge/account/**; Web:src/ArcForges.Web.App/** (CSP and budget configuration only)
Shared resources (follow the owner protocol): RES-web-app-routing (append): The application shell task owns root route registration; each surface adds its own route module and per-origin edge directory.; RES-web-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: WEB.18

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Policy header verification against the published profile build, with an exact CSP token-set assertion; bundle secret scan; sandbox escape test on hostile content; budget measurements with regression gate (xUnit, offline and CI-eligible); in-browser CSP proof local opt-in under PRF.11.
Completion evidence for the ledger: Policy headers, bundle secret scan and budget measurements
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): The 'no default inline script' wording becomes the Blazor CSP rule of P2-021 item 2: wasm-unsafe-eval plus required hashes, never unsafe-eval or unsafe-inline. The React budgets (apps/app/budgets.json: initialJsGzip 116363 account, 144698 chat, regressionPercent 10) are re-baselined only by the reviewed AL-06 record and never silently.
```

```text
Execute ArcForges delivery task WEB.17 — Offline, degradation and accessibility (account).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-17).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-17 (python tools/delivery.py claim WEB.17 --worker <name>); task branch task/web-17 in Web; ledger record ledger/tasks/web-17.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Honest offline behaviour in the Blazor Account profile, in memory only: no service worker and no persistent account cache (WCI-05). When the connection drops, the profile shows an honest offline state and keeps unsent input in live component state for the current page session; a cloud-outage state naming unavailable capabilities with reasons rather than blanking; and full keyboard-only accessibility on every major workflow.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.07 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.07

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.12: account/security surfaces
- [artifact] WEB.13: workspace/storage surfaces
- [artifact] WEB.14: commerce surfaces
- [artifact] WEB.15: data surfaces
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.App/**; Web:tests/ArcForges.Web.App.Tests/**
Unblocks: WEB.18

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline-behaviour tests (bUnit/xUnit): offline state shown, unsent input kept across a simulated connection loss within the page session, no service worker registered and no browser-storage write asserted; cloud-outage-no-blank test; accessibility CI-gated semantic checks (WEB.06) and a manual pass.
Completion evidence for the ledger: Offline, outage and accessibility results
Notes: Planning repair 2026-10-08 (DLV-34; P2-021, WCI-05): The offline criterion is reconciled to the online-only decision. Offline behaviour in the Blazor profiles is in memory only (no service worker, no persistent cache), so unsent input survives a connection loss within the page session but not a reload; a draft that survives reload would need a reviewed WCI-05 decision. The UI port targets the Blazor Account profile components.
```

```text
Execute ArcForges delivery task WEB.18 — Verify the owned Account artifact and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-18).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-18 (python tools/delivery.py claim WEB.18 --worker <name>); task branch task/web-18 in Web; ledger record ledger/tasks/web-18.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Real browser evidence against the AOT release closes cookie secrecy, CSRF, expiry/revocation, privacy/export and admission/usage display; the account deployment profile is the sole account application with no AGPL import into Mobile.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.90 (full; final-review closure: 08-security-architecture account/provider closure, scoped-token display-once, cancellation restricted route): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.90
- WP-48:required-implementation-and-closure-from Required implementation and closure from the final review: 08-security-architecture account/provider closure, scoped-token display-once, cancellation restricted route (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md, package-level obligation
- WP-48:browser-matrix-acceptance-paragraph-brow Browser matrix acceptance paragraph (browser-support.v1 for the account output) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md, package-level obligation

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.11: session/step-up
- [artifact] WEB.12: security surfaces
- [artifact] WEB.13: workspace surfaces
- [artifact] WEB.14: commerce surfaces
- [artifact] WEB.15: data surfaces
- [artifact] WEB.16: origin security
- [artifact] WEB.17: resilience
- [artifact] WEB.29: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.App/**
Unblocks: REL.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Real browser against the AOT release: cookie secrecy, CSRF, expiry/revocation, privacy/export and admission/usage display — local opt-in per P2-017
Completion evidence for the ledger: Owned-artifact-and-real-integration receipt; contributes its scoped evidence toward PG-23 (closed later at WP50, not here)
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): The phrase AOT release refers to the Cloud Native AOT backend, not to Web, so it is unchanged. The Web profile is Blazor WebAssembly standalone with RunAOTCompilation=false by default; any WASM AOT adoption requires the PRF.11 benchmark record.
```

```text
Execute ArcForges delivery task WEB.19 — Chat shell: route composition and design-system integration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-19).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-19 (python tools/delivery.py claim WEB.19 --worker <name>); task branch task/web-19 in Web; ledger record ledger/tasks/web-19.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Chat routes are composed in the same ArcForges.Web.App Blazor WebAssembly codebase using owned ArcForges.Web.Ui components and the generated C# gRPC-Web client. Account and Chat assets, cookies, query scopes and public config are independently selected and validated (separate profile output; no chat code in the account profile). Responsive conversation navigation, composer and task panel, and native-product handoff work with keyboard and reduced-motion support.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.00

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.08: design system tokens/components
- [artifact] WEB.10: account shell and apps/app workspace registration
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.App/Features/Chat/**
Shared resources (follow the owner protocol): RES-web-app-routing (append): The application shell task owns root route registration; each surface adds its own route module and per-origin edge directory.; RES-web-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-web-shared-ui (append): The design-system task owns the shared UI package; surfaces request components through it; additions after it are additive.
Unblocks: WEB.20, WEB.21, WEB.22, WEB.23, WEB.25, WEB.30, WEB.31, WEB.32, WEB.33

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Production route and profile inspection; approved light, dark and narrow-screen visual baselines; keyboard, touch and long-text states; xUnit source and dependency assertion that no provider or Harness implementation enters the browser profile.
Completion evidence for the ledger: Cross-profile isolation results
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Chat is the second Blazor profile of the same ArcForges.Web.App codebase (not re-registered). The route-composition and design-system criteria are unchanged.
```

```text
Execute ArcForges delivery task WEB.20 — Conversation and generated output streams.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-20).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-20 (python tools/delivery.py claim WEB.20 --worker <name>); task branch task/web-20 in Web; ledger record ledger/tasks/web-20.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: The full Chat UI uses annex-10 gRPC-Web binary output and event streams (Grpc.Net.Client.Web; server streaming through the .NET 10 browser streaming client, with the grpc-web-text variant on server-stream routes only if the PRF.11 decision records it, and then its framing variant is recorded in the wire registry before the stream UI ships) with durable recovery. Cloud history is authoritative except memory-only temporary UI, and an interrupted stream is always shown as interrupted, never complete.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.01 (all work except the parts mapped to WEB.27): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.01

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.19: chat shell + real deployed WP23/24 transport (inherited via WEB.10)
- [artifact] PRF.11: the binary-versus-text server-stream decision and the browser streaming proof
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] WEB.27: real CF Harness admission/generation/tool loop
- [integration] SRCH.90: the companion assistant answers that cite search, delivered search surface (SW-06)

Permitted write scope: Web:src/ArcForges.Web.App/Features/Chat/**; Web:tests/ArcForges.Web.App.Tests/**
Permitted substitutes (never real integration evidence): SUB-fixture-turn-endpoint: client-side session/event/output/upload handling, typed state transitions, reconnection -- runs no model/planner/admission/metering itself Real producer ['HAR.00', 'HAR.02', 'HAR.03']; removed by HAR.05
Unblocks: WEB.24, WEB.26, WEB.27

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Generated event-contract and recovery tests (byte offsets, reconnect and gaps, duplicate delivery, loss of authorization) as xUnit and bUnit tests over the generated C# event contract; browser-support.v1 polling-fallback behaviour (EventService.Poll every 10s +/-20% jitter, ExecutionService.ReadOutput every 5s after the 45s stream-silence timeout), unchanged.
Completion evidence for the ledger: Streaming, interruption and partial-message results
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): The polling constants are kept verbatim. Blazor browser server streaming is unverified in the research and is decided by PRF.11. The WEB.27 completion edge and the SUB-fixture-turn-endpoint substitute are unchanged. Planning repair 2026-10-09 (P2-026; scope correction): realtime server streaming is V1 (S3), and the SRCH.90 completion verifies companion answers (S13).
```

```text
Execute ArcForges delivery task WEB.21 — Tasks, approval and steering.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-21).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-21 (python tools/delivery.py claim WEB.21 --worker <name>); task branch task/web-21 in Web; ledger record ledger/tasks/web-21.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Task/run/step/tool-call surfaces with progress; approve/reject/cancel/pause/retry/steer as idempotent commands; local-presence-required operations are clearly refused with an explanation; no missed notification loses a pending approval.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.02 (all work except the parts mapped to WEB.27, WEB.28): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.02

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.19: chat shell
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] WEB.28: real device bridge
- [integration] WEB.27: real Harness planning/tool-proposal loop

Permitted write scope: Web:src/ArcForges.Web.App/Features/Tasks/**; Web:tests/ArcForges.Web.App.Tests/**
Unblocks: WEB.24, WEB.26, WEB.27, WEB.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Idempotency-per-control, local-presence-negative, approval-expiry and durable-attention tests
Completion evidence for the ledger: Control idempotency, local-presence and attention-durability results
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Task, approval and steering surfaces are Blazor components. The idempotency, local-presence and attention-durability criteria are unchanged.
```

```text
Execute ArcForges delivery task WEB.22 — Artifacts and sandboxing.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-22).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-22 (python tools/delivery.py claim WEB.22 --worker <name>); task branch task/web-22 in Web; ledger record ledger/tasks/web-22.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Artifact preview runs inside an isolated sandbox (a sandboxed frame whose CSP is re-proven under PRF.11, with JavaScript interop only at that audited sandbox point) so untrusted content never executes in the application origin. Downloads verify permission at access, and no public share links exist in V1.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.03

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.19: chat shell
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.App/Features/Artifacts/**
Unblocks: WEB.24, WEB.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Sandbox-escape attempt with hostile content; permission-at-access test (bUnit/xUnit); existence-disclosure test on a denied resource; public-share-link absence assertion.
Completion evidence for the ledger: Sandbox escape, permission-at-access and share-link absence results
Notes: Self-contained: mostly a client-side iframe/CSP isolation mechanism plus WP25 resource tickets already inherited via the account shell; does not need WP26 or WP52. Planning repair 2026-10-08 (DLV-34; P2-021): The isolation mechanism moves from the React host to the Blazor host with a re-proven sandbox CSP. The sandbox-escape, permission-at-access and share-link criteria are unchanged. Planning repair 2026-10-09 (P2-026; scope correction): still-image attachments are shown as metadata cards (type, name and size by magic-byte sniffing) with no decoded still-image preview in V1 Web (S1); the sandboxed artifact preview is unchanged.
```

```text
Execute ArcForges delivery task WEB.23 — One-application remote control.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-23).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-23 (python tools/delivery.py claim WEB.23 --worker <name>); task branch task/web-23 in Web; ledger record ledger/tasks/web-23.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Device applications are listed, an explicit authorized product/installation is selected and frozen per task target; no browser local connection, another-product tool or local-only desktop chat access exists; an offline target shows an honest queued state with expiry.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.04 (all work except the parts mapped to WEB.28): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.04

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.19: chat shell + real device-presence API (inherited)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] WEB.28: real device bridge dispatch

Permitted write scope: Web:src/ArcForges.Web.App/Features/Devices/**
Unblocks: WEB.24, WEB.26, WEB.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Scope/permission, wrong-or-stale-target, loss/retry and expiry scenarios against the exact real artifact/owner boundary
Completion evidence for the ledger: Offline-target queueing and no-local-connection results
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Device list and picker are Blazor components. The scope, wrong-target and expiry criteria are unchanged.
```

```text
Execute ArcForges delivery task WEB.24 — Offline, degradation and accessibility (chat).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-24).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-24 (python tools/delivery.py claim WEB.24 --worker <name>); task branch task/web-24 in Web; ledger record ledger/tasks/web-24.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Honest offline messaging in the Blazor Chat profile, in memory only (no service worker, no persistent chat cache; WCI-05): unsent input is kept in live component state for the current page session; realtime loss degrades to polling with backfill using the WEB.20 constants; a cloud outage reports unavailable capabilities rather than blanking; every core workflow completes by keyboard.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.05

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.20: streaming UI
- [artifact] WEB.21: tasks UI
- [artifact] WEB.22: artifacts UI
- [artifact] WEB.23: device UI
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.App/**; Web:tests/ArcForges.Web.App.Tests/**
Unblocks: WEB.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline and reconnection tests (bUnit/xUnit: offline messaging, in-session unsent input kept, no service worker, no persistent chat cache written); polling-degradation test; cloud-outage test; accessibility CI-gated semantic checks (WEB.06) and a manual pass.
Completion evidence for the ledger: Offline, degradation, convergence and accessibility results
Notes: Planning repair 2026-10-08 (DLV-34; P2-021, WCI-05): The offline criterion is reconciled to in-memory offline behaviour as in WEB.17. Realtime-to-polling degradation keeps the WEB.20 polling constants.
```

```text
Execute ArcForges delivery task WEB.25 — Performance budgets (chat).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-25).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-25 (python tools/delivery.py claim WEB.25 --worker <name>); task branch task/web-25 in Web; ledger record ledger/tasks/web-25.md.
Kind/size: feature/S. Baseline: not-started.
Outcome: Bundle size (compressed Blazor WebAssembly download and startup), first-interactive and interaction-responsiveness budgets are measured per release candidate with a regression gate that catches a deliberate regression. The Blazor WebAssembly budgets are set by a reviewed AL-06 re-baseline record (owner PRF.11); the React numbers are not carried over silently.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.06

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.19: chat shell
- [artifact] PRF.11: the measured Blazor WebAssembly profile size and startup and the AL-06 re-baseline record
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.App/Features/Chat/**; Web:tools/ArcForges.Web.Tooling/Budgets/**
Shared resources (follow the owner protocol): RES-web-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: WEB.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Budget measurements per release candidate; regression-gate negative test
Completion evidence for the ledger: Budget measurements and regression-gate negative test
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): These are performance budgets, not the cost-control budgets. The regression-gate criterion is kept and the React baseline is re-baselined by reviewed record only.
```

```text
Execute ArcForges delivery task WEB.26 — Verify the owned Chat artifact and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-26).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-26 (python tools/delivery.py claim WEB.26 --worker <name>); task branch task/web-26 in Web; ledger record ledger/tasks/web-26.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: A full real admitted CF turn/tool/approval/reconnect sequence is exercised in a browser using the fixed same-origin session and generated AI gRPC-Web route; a blocked/expired live stream reconciles to the authoritative result without leaking session credentials.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.90
- WP-49:browser-matrix-acceptance-paragraph-brow Browser matrix acceptance paragraph (browser-support.v1 for the chat output) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md, package-level obligation

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.20: streaming
- [artifact] WEB.21: tasks/approval
- [artifact] WEB.22: artifacts
- [artifact] WEB.23: remote control
- [artifact] WEB.24: resilience
- [artifact] WEB.25: budgets
- [artifact] WEB.32: package task delivered
- [artifact] WEB.33: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] WEB.27: real Harness

Permitted write scope: Web:src/ArcForges.Web.App/**
Unblocks: REL.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Full real admitted CF turn/tool/approval/reconnect in a browser — local opt-in per P2-017
Completion evidence for the ledger: Owned-artifact-and-real-integration receipt; contributes its scoped evidence toward PG-23 (closed later at WP50)
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): The integration receipt is unchanged; the browser run is against the Blazor Chat profile and the generated C# AI gRPC-Web route.
```

```text
Execute ArcForges delivery task WEB.27 — Real CF Harness generation/tool loop observed end to end in the browser.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-27).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-27 (python tools/delivery.py claim WEB.27 --worker <name>); task branch task/web-27 in Web; ledger record ledger/tasks/web-27.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: real admitted generation and tool proposal replace the contract-bound fixture turn endpoint in Chat

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.01 (real-integration closure): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.01
- WP-49.02 (real-integration closure): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.02

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.20: real, delivered outcome of WEB.20 (Conversation and generated output streams)
- [artifact] WEB.21: real, delivered outcome of WEB.21 (Tasks, approval and steering)
- [artifact] HAR.00: real, delivered outcome of HAR.00 (Turn loop, tool batching and bounds (RunWorkflow core))
- [artifact] HAR.03: real generated streaming and durable output
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: HAR.05, WEB.20, WEB.21, WEB.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: real admitted generation and tool proposal replace the contract-bound fixture turn endpoint in Chat
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Stack-neutral acceptance; no change to outcome, validation or evidence. The browser run is against the C# Chat profile (WEB.19/WEB.20) and the generated C# clients.
```

```text
Execute ArcForges delivery task WEB.28 — Real desktop tool dispatch from the browser companion.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-28).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-28 (python tools/delivery.py claim WEB.28 --worker <name>); task branch task/web-28 in Web; ledger record ledger/tasks/web-28.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: a browser-initiated remote task actually reaches a desktop through the durable bridge

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.02 (device-dispatch closure): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.02
- WP-49.04 (real-integration closure): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.04

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.21: real, delivered outcome of WEB.21 (Tasks, approval and steering)
- [artifact] WEB.23: real, delivered outcome of WEB.23 (One-application remote control)
- [artifact] DEV.02: the real durable target queue
- [artifact] DEV.03: real owner reauthorization on the desktop
- [artifact] DEV.06: real remote approval and steering
- [artifact] DEV.07: real offline expiry and unknown-effect recovery
- [artifact] DEV.12: the cross-repository (toolRequestId, attemptId, commandId) agreement
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: WEB.21, WEB.23

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: a browser-initiated remote task actually reaches a desktop through the durable bridge
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Stack-neutral acceptance; no change to outcome, validation or evidence. The browser companion is the C# Blazor Chat profile.
```

```text
Execute ArcForges delivery task WEB.29 — Real commerce/policy provider evidence for the account portal.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-29).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-29 (python tools/delivery.py claim WEB.29 --worker <name>); task branch task/web-29 in Web; ledger record ledger/tasks/web-29.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: hosted checkout, entitlement reasons and rate-limit/recovery text reflect a real test-mode ledger and policy service, not contract fixtures

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.04 (real-provider-evidence closure): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.04

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.14: real, delivered outcome of WEB.14 (Subscription, capacity, credits and hosted checkout)
- [artifact] COM.14: real, delivered outcome of COM.14 (Technical commerce closure and live-gate staging)
- [artifact] POL.08: real, delivered outcome of POL.08 (Publication, staleness and last-known-good (server side))
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: WEB.18

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: hosted checkout, entitlement reasons and rate-limit/recovery text reflect a real test-mode ledger and policy service, not contract fixtures
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Stack-neutral acceptance; no change to outcome, validation or evidence. The account portal under test is the Blazor Account profile.
```

```text
Execute ArcForges delivery task WEB.30 — Real Blazor WebAssembly Web client against deployed browser session/PublicApi/realtime.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-30).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web). Also touches: Cloud.
Claim and handoff record: claims/web-30 (python tools/delivery.py claim WEB.30 --worker <name>); task branch task/web-30 in Web; ledger record ledger/tasks/web-30.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Real C# gRPC-Web client (Grpc.Net.Client.Web, generated from Contracts) with cookie, CSRF and Origin session behaviour and realtime streams against the deployed Cloud, beyond fixture-backed proofs (no fixture or test double stands in for the deployed ingress).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.05 (Web real-consumer integration): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.05

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.19: real, delivered outcome of CLOUD.19 (Browser cookie-session adapter and full account-surface closure)
- [artifact] CLOUD.26: real, delivered outcome of CLOUD.26 (Generated C#/TypeScript/Kotlin clients against Identity/Workspace/Device)
- [artifact] CLOUD.29: real, delivered outcome of CLOUD.29 (Stream connection and authentication (EventService.Watch/ExecutionService.WatchOutput shells))
- [artifact] WEB.07: real, delivered outcome of WEB.07 (Independence and atomic deployment)
- [artifact] WEB.14: real, delivered outcome of WEB.14 (Subscription, capacity, credits and hosted checkout)
- [artifact] WEB.19: real, delivered outcome of WEB.19 (Chat shell: route composition and design-system integration)
- [artifact] PRF.11: the Blazor WebAssembly production proof (PRF.11, successor of the superseded React PRF.08)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: CLOUD.28, WEB.31

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: Real C# gRPC-Web client, cookie/CSRF/Origin session behaviour and realtime streams against the deployed Cloud, beyond fixture-backed proofs.
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): The React/MSW wording is replaced by the C# Blazor client: the same real deployed session, PublicApi and realtime criteria. SUB-web-msw-fixtures is restated for the C# client; its test-only rule is kept. PRF.08 is retargeted to PRF.11.
```

```text
Execute ArcForges delivery task WEB.31 — Full browser-support.v1 matrix across all Web-facing outputs.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-31).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web). Also touches: Cloud.
Claim and handoff record: claims/web-31 (python tools/delivery.py claim WEB.31 --worker <name>); task branch task/web-31 in Web; ledger record ledger/tasks/web-31.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Supported/degraded/blocked behavior across every output's flows on real browser/OS patches; WP-50 joins all production hashes and real browser evidence

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23:browser-matrix-acceptance-appendix-full Browser matrix acceptance appendix, full cross-area join (Browser matrix acceptance appendix, full cross-area join): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md, package-level obligation

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] OPS.05: real, delivered outcome of OPS.05 (Operator console and support access)
- [artifact] WEB.07: real, delivered outcome of WEB.07 (Independence and atomic deployment)
- [artifact] WEB.14: real, delivered outcome of WEB.14 (Subscription, capacity, credits and hosted checkout)
- [artifact] WEB.19: real, delivered outcome of WEB.19 (Chat shell: route composition and design-system integration)
- [artifact] WEB.30: the real Blazor WebAssembly client against the deployed browser session
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.28: the WP-23 browser-matrix Cloud part accepted

Permitted write scope: 

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: Supported/degraded/blocked behavior across every output's flows on real browser/OS patches; WP-50 joins all production hashes and real browser evidence
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Stack-neutral acceptance; no change to outcome, validation or evidence. The browser matrix runs against the C# Web profiles. Planning repair 2026-10-08 (DLV-34; P2-023): The browser-support matrix has no macOS or Safari rows, because macOS is outside the delivery scope. Supported, degraded and blocked criteria are otherwise unchanged, and the matrix runs against the C# Blazor profiles. Planning repair 2026-10-09 (P2-026; scope correction): reduced: Safari rows, macOS OS entries and any macOS or iOS Safari claim or test are out of scope, not completed (P2-023).
```

```text
Execute ArcForges delivery task WEB.32 — ArcScope workspace in the Web companion: library and reports.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-32).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-32 (python tools/delivery.py claim WEB.32 --worker <name>); task branch task/web-32 in Web; ledger record ledger/tasks/web-32.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: The Web ArcScope library: projects, sessions, findings and annotations, report reading with provenance and stored chart snapshots, exported-report download through resource tickets, sessions and reports attached to assistant conversations, and the ArcScope notification kinds. Under P2-022 the exported report PDF (arcscope.report.pdf.v1) is presented only through the browser's built-in PDF viewer (a sandboxed iframe with CSP isolation where it can be enforced, otherwise download or open; requirements/12 line 421) or downloaded as an opaque file; the Web companion has no app-side PDF parser, text extraction, tile rendering or PDF library, and no native PDF preview is kept.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.07 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.07

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.19: the companion route shell and design-system integration
- [contract] CON.24: the generated C# library operations
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.68: the deployed library read model
- [integration] SCOPE.22: the delivered desktop project/session and report publication adapter

Permitted write scope: Web:src/ArcForges.Web.App/Features/Scope/**
Unblocks: WEB.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: A report synced from ArcScope desktop found, read with provenance (in the Web report reader or through the browser's built-in PDF viewer) and downloaded on Web with provenance; revocation, ticket expiry and accessibility results; a negative check that the Web App output references no PDF parser or renderer.
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): The ArcScope library views are Blazor components in the Web companion. The generated-operation dependency is now the C# client. Acceptance is unchanged.
```

```text
Execute ArcForges delivery task WEB.33 — Cloud simulator console in the Web companion.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-33).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-33 (python tools/delivery.py claim WEB.33 --worker <name>); task branch task/web-33 in Web; ledger record ledger/tasks/web-33.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: The simulator console: definitions, immutable scenario versions with validation errors, start, pause, resume and cancel with expectedRev and legal predecessor-state guards, run state with complete-or-partial extent, and the committed segment manifest with resumable, hash-verified downloads. Run history is discovered through simulation.listRuns on a fresh session.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.08 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.08

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.19: the companion route shell and design-system integration
- [contract] CON.21: the generated C# simulation operations
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] SIM.05: the deployed simulation operations

Permitted write scope: Web:src/ArcForges.Web.App/Features/Simulation/**
Unblocks: WEB.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: A scenario created and run from the browser with every desktop off, completed or cancelled with the correct extent, and its committed segments downloaded and verified. Authorized run discovery, filter paging and denied cross-workspace access.
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): The simulator console is a Blazor route set of the Web companion. Its run-control, extent and segment-download acceptance is unchanged.
```

```text
Execute ArcForges delivery task WEB.40 — Blazor migration of the existing Web (C# static Site, Blazor WebAssembly profiles, C# policy).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\web.md (anchor task-web-40).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-40 (python tools/delivery.py claim WEB.40 --worker <name>); task branch task/web-40 in Web; ledger record ledger/tasks/web-40.md.
Kind/size: producer/XL. Baseline: not-started.
Outcome: Migrates the existing Web repository to the C#-first stack with equal acceptance. (1) The C# static Site generator (ArcForges.Web.Site, first-party Razor HtmlRenderer) reproduces the current public pages (/, /hello, /cloud-hello and the documentation, legal and download inventory) with no runtime JavaScript (TB-01) and replaces apps/site. (2) Blazor WebAssembly standalone Account and Chat deployment profiles (ArcForges.Web.App, RunAOTCompilation=false by default) replace apps/app with identical cookie-session, antiforgery/CSRF, Origin, exact-value and typed-failure semantics. The Operations console keeps its own standalone Blazor WebAssembly profile (ArcForges.Web.Operations) on a separate origin and identity: this task creates only its skeleton, and the operator features are built by OPS.05. (3) packages/ui becomes the Razor class library ArcForges.Web.Ui. (4) Every existing test whose subject stays in V1 is ported one-for-one to xUnit (contract) or bUnit (components); the Node provenance and policy tests are out under S17(a), with Microsoft.Playwright for .NET kept as local opt-in test-only tooling (axe-core injected only into the page under test; no npm-hosted test tooling remains). (5) CI and deploy build the C# outputs once and promote the same bytes to Cloudflare Static Assets through the unchanged thin worker/index.js. The existing main-push Cloudflare deploy job in .github/workflows/ci.yml stays as a deployment step outside validation (section 6 decision 2); its rollback acceptance is a named gate recorded by a local operator run receipt. (6) Every NuGet package in the closure is admitted with provenance and licence receipts under eng/policy. (7) The GOV.11 policy and its C# successor are out of scope under S17(a), not completed. (8) JavaScript interop is limited to the listed audited points (WebAuthn, clipboard, download and share, sandboxed preview).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.02 (wire the forbidden-term scanner into Web's own PR build (carried from GOV.11; kept under P2-026 review fix as the shared published naming check, not the GOV.11 policy suite, which is out)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.03: build governance, packaging policy and analyzers (inherited)
- [contract] CON.07: generated C# gRPC-Web session and device client and the BrowserSession HTTP exception codecs from the published Contracts NuGet candidate (precondition: the NuGet identity is verified at start from the CON.07 publication record)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.Site/** (C# HtmlRenderer static generator replacing apps/site); Web:src/ArcForges.Web.App/** (Blazor WebAssembly Account and Chat profiles replacing apps/app); Web:src/ArcForges.Web.Ui/** (Razor class library replacing packages/ui); Web:tests/ArcForges.Web.Site.Tests/**; Web:tests/ArcForges.Web.App.Tests/**; Web:tests/ArcForges.Web.Ui.Tests/**; Web:Directory.Packages.props (new central NuGet pins); Web:nuget.config (new locked package sources); Web:src/**/packages.lock.json (per-project NuGet lock files); Web:win.slnx (C# projects replace the esproj entry); Web:ArcForges.Web.esproj (retired after parity, replaced by csproj references); Web:Directory.Build.targets (keep the AGPL/Apache licence-boundary MSBuild targets); Web:package.json and Web:package-lock.json (reduced to wrangler, Node build and deploy tooling only; no npm-hosted test tooling remains, brief section 5 item 8); Web:apps/** and Web:packages/ui/** (React sources removed after the one-for-one port; history stays in git); Web:tooling/*.ts, Web:tests/unit/*.ts, Web:tests/fixtures/*.ts, Web:vitest.config.ts, Web:tsconfig.json, Web:biome.json (retained where S17(a) takes their port out of scope; otherwise removed after the one-for-one port); Web:tests/browser/** (Microsoft.Playwright for .NET, test-only local opt-in tooling); Web:wrangler.json; Web:worker/** (thin adapter kept); Web:.github/workflows/ci.yml; Web:eng/policy/** (dependency-policy.json NuGet admissions); Web:eng/policy/dependency-reviews/** (immutable NuGet closure receipts); Web:eng/provenance/** (NuGet closure provenance records; historical records kept); Web:.gitleaks.toml; Web:docs/** (factual updates to development, deploying, provenance and validation); Web:src/ArcForges.Web.Operations/** (Operations profile skeleton only: project, shell routes and separate-origin configuration; no operator feature code); Web:tests/ArcForges.Web.Operations.Tests/** (skeleton tests only); Web:tests/provenance/** (retained unchanged: the xUnit successor for every provenance test is out of scope under S17(a), not completed); Web:.github/dependabot.yml (npm groups react-and-router, contracts, cloudflare and tooling retarget to the NuGet and wrangler closure in the same change; no open Dependabot pull request is touched)
Shared resources (follow the owner protocol): RES-web-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.; RES-web-app-routing (append): The application shell task owns root route registration; each surface adds its own route module and per-origin edge directory.; RES-web-shared-ui (append): The design-system task owns the shared UI package; surfaces request components through it; additions after it are additive.
Unblocks: CLOUD.85, CON.40, OPS.05, PRF.11, WEB.01, WEB.08, WEB.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Windows build and test of win.slnx with the pinned .NET 10 SDK and central package management (dotnet build and test, offline after an approved restore). One-for-one port table: every retired TS or React test whose subject stays in V1 has an xUnit or bUnit successor with the same positive and negative cases (tests/unit and tests/fixtures; the Node tooling and provenance tests named in the notes are out under S17(a)). The migrated public page inventory is compared with the React output before apps/site is removed. Account and Chat profile tests for identical session, CSRF, exact-value and typed-failure semantics. NuGet closure licence and provenance receipts. The published forbidden-term scanner runs as a failing check in Web's own PR build (WP-05.02). Microsoft.Playwright for .NET only as local opt-in test tooling, with axe-core injected only into the page under test; the CI accessibility gate is the xUnit/bUnit semantic set (section 6 decision 3). The existing main-push Cloudflare deploy job is a deployment step outside validation (section 6 decision 2). No hosted browser, device or live-service CI (P2-017). Linux-affected checks run once in WSL2 Debian on a Linux-native filesystem (P2-024). The Operations profile skeleton is covered by the same exact CSP token-set assertion as the Account and Chat profiles (script-src 'self' 'wasm-unsafe-eval' plus required hashes; never unsafe-eval or unsafe-inline) and contains no operator feature code. Dependabot: .github/dependabot.yml ports its npm groups to NuGet and wrangler groups in the same change as the closure. Any Gitleaks generic-api-key exception change needs named authority, independent exact-head review and retained CI before merge.
Completion evidence for the ledger: One-for-one port table with a successor for every retired test whose subject stays in V1; byte comparison of the migrated public page inventory; CI run receipt for the C# build; NuGet closure provenance and licence receipts; coordination note with Cloud on CLOUD.71 bundle naming.
Notes: Decisions this task depends on: P2-021 items 2 and 8 (Microsoft.Playwright for .NET stays test-only local tooling, and the Blazor-free public Site per TB-01); brief section 5 item 8 (no npm-hosted test tooling remains); brief section 6 decision 3 (accessibility tooling: the CI gate is the bUnit/xUnit semantic assertion set, and axe-core is local opt-in only through Microsoft.Playwright for .NET, injected only into the page under test); section 6 decision 2 (the existing main-push Cloudflare deploy job stays as a deployment step). Under the same decision 3 no accessibility analyzer NuGet package is in the CI gate. The CON.07 NuGet identity is a start precondition verified from the CON.07 publication record. The port of tooling/*.ts to C# is out of scope under S17(a), not completed. It creates the Operations profile skeleton that OPS.05 builds on. Bundle naming coordinates with CLOUD.85 and CLOUD.71. CON.40 (Contracts consumer migration) starts after WEB.40 delivers, so this task does not start on CON.40. Decision basis: P2-021 (decision obligations are reserved for adoption and governance tasks, so the decision is cited here rather than as an obligation). Planning repair 2026-10-09 (P2-026; scope correction): reduced: OPS.11 package-review routes are out of scope, not completed. Tests whose only subject is retired React, Vite or npm tooling or an excluded product (ArcSlate, ArcNotes, macOS) retire with an explicit successor record, not a port. GOV.11 is out; its C# successor is item (7) of this task. Planning repair 2026-10-09 (P2-026; scope correction, brief section 11 S17(a)): reduced: the remaining Node TypeScript build, policy and provenance tooling port is out of scope, not completed. That covers dependency-policy.ts, provenance.ts, licence-boundary.ts, project.ts, build-identity.ts, cloudflare.ts and candidate.ts (tools/ArcForges.Web.Tooling is not created), the node:test provenance tests build-identity, legal-path, source, csharp-candidate, lock-provenance and cloudflare-delivery, and the xUnit successor for every provenance test. Node stays for wrangler and these build tools; product and business code stays C# (Blazor) and the Worker stays a thin adapter. The outcome and validation clauses that name that port are carved out by this note, not completed. Planning repair 2026-10-09 (P2-026 review fix; brief section 11 S17(a)): the GOV.11 policy and its C# successor are out of scope, so the outcome no longer requires them, the validation no longer requires the policy suite, the GOV.11 review standard or the policy negative-example evidence, the writes no longer name tools/ArcForges.Web.Tooling or tests/ArcForges.Web.Policy.Tests, and the web-csharp-policy-suite provide and the obligations carried from GOV.11 (WP-05.01 and WP-05.04 for the Web slice, and the package-level Web assertion) are removed; WP-05.02 stays as the Web PR build obligation for the shared naming scanner. The WP-05.01 and WP-05.04 substeps stay owned by the in-scope slice tasks (GOV.07, GOV.09, AND.40). Gitleaks exception changes keep named authority, independent exact-head review and retained CI.
```
