# ArcForges delivery task prompts — Web

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Web

```text
Execute ArcForges delivery task WEB.01 — React static generation and determinism engine.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-01 (python tools/delivery.py claim WEB.01 --worker <name>); task branch task/web-01 in Web; ledger record ledger/tasks/web-01.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: React Router build-time pre-rendering (SSR disabled) generates the full public locale/URL inventory, documentation versions, sitemap, metadata and redirects, deterministically, with no Account/Chat route bundle or private config leaking into the static output.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.00

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.03: Node/npm workspace and toolchain pins
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:apps/site/**
Shared resources (follow the owner protocol): RES-contract-consumer-pins (append): A consumer task updates the pin it needs through a reviewed dependency change to the exact published candidate containing its closure; no consumer pins an unpublished closure or references Contracts source.
Unblocks: WEB.02, WEB.03, WEB.04, WEB.05, WEB.06, WEB.07

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Two full builds with identical inputs compared byte-for-byte; no-script navigation/content tests; single-content-change diff; build with network disabled after approved restore — CI-eligible offline checks
Completion evidence for the ledger: Determinism comparison and diff-minimality results
Notes: Its only real start need (WP00/WP02) is already satisfied; the current serial plan defers WP47 until after WP40, but nothing blocks starting this immediately.
```

```text
Execute ArcForges delivery task WEB.02 — Versioned public content and pricing inputs (catalogue.json).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-02 (python tools/delivery.py claim WEB.02 --worker <name>); task branch task/web-02 in Web; ledger record ledger/tasks/web-02.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Catalogue, release metadata, changelog and legal versions are consumed from declared versioned local inputs with no live provider fetch during build; the pricing projection shows its effective version/time.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.01

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.01: static generator
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:apps/site/content/**; Web:apps/site/app/catalogue.json
Unblocks: WEB.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Hard-coded-version/price scan; comparison of public projection to the selected approved snapshot — offline
Completion evidence for the ledger: No independently hard-coded product version/private supplier price
Notes: Private candidate builds may use named test-only offer/release fixtures per WP-47.01; the real WP42/44 numeric join for public promotion is explicitly deferred to WP50, not required to close this task's own gate.
```

```text
Execute ArcForges delivery task WEB.03 — Rendering and performance.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-03 (python tools/delivery.py claim WEB.03 --worker <name>); task branch task/web-03 in Web; ledger record ledger/tasks/web-03.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Above-the-fold content ships in delivered HTML, assets are content-hashed with short-lived HTML caching, no blocked third-party resource sits on the critical path, and p75 LCP/INP/CLS budgets are met.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.02

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.01: static generator
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:apps/site/**; Web:tooling/**
Shared resources (follow the owner protocol): RES-web-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: WEB.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): No-script render test; critical-path resource audit; p75 performance measurement; global-reachability check on every third-party host — offline/lab
Completion evidence for the ledger: No-script render, critical-path audit and performance measurements
```

```text
Execute ArcForges delivery task WEB.04 — Internationalisation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-04 (python tools/delivery.py claim WEB.04 --worker <name>); task branch task/web-04 in Web; ledger record ledger/tasks/web-04.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Locale-scoped URLs with alternate-language annotations, no client-only switching and no trapping redirect; every user-visible string, including generated pages, is localisable.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.03

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.01: static generator
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:apps/site/**
Unblocks: WEB.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Locale routing/annotation tests, no-trap assertion, pseudo-localisation pass — offline
Completion evidence for the ledger: Locale routing, no-trap and pseudo-localisation results
```

```text
Execute ArcForges delivery task WEB.05 — Documentation, downloads and legal surfaces.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-05 (python tools/delivery.py claim WEB.05 --worker <name>); task branch task/web-05 in Web; ledger record ledger/tasks/web-05.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Versioned per-product documentation, a no-account-gate download surface serving signed artifacts with published hashes, an update feed surface, and versioned legal pages with effective dates.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.04

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.01: static generator
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:apps/site/content/**; Web:apps/site/app/routes/**
Unblocks: WEB.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Documentation version routing; download integrity verification against published hashes; no-account-gate assertion; legal version-history tests — offline against labelled fixtures
Completion evidence for the ledger: Download integrity, no-gate and legal versioning results
Notes: Private candidate download fixtures are labelled; public promotion with real signed Desktop/Android artifacts is joined at WP50, not required to close this task.
```

```text
Execute ArcForges delivery task WEB.06 — Accessibility and analytics.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-06 (python tools/delivery.py claim WEB.06 --worker <name>); task branch task/web-06 in Web; ledger record ledger/tasks/web-06.md.
Kind/size: feature/S. Baseline: not-started.
Outcome: Accessibility semantics and keyboard-only navigation on every page; minimal privacy-preserving analytics with no cross-site identifier and no consent wall.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.05

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.01: static generator
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:apps/site/**
Unblocks: WEB.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Automated accessibility checks (axe-core, already a pinned devDependency) plus a dated manual verification; analytics payload audit — offline
Completion evidence for the ledger: Accessibility checks pass with a dated manual record; analytics carry no cross-site identifier
```

```text
Execute ArcForges delivery task WEB.07 — Independence and atomic deployment.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-07 (python tools/delivery.py claim WEB.07 --worker <name>); task branch task/web-07 in Web; ledger record ledger/tasks/web-07.md.
Kind/size: release/S. Baseline: not-started.
Outcome: The site remains fully available during a full Cloud outage, deploys atomically per surface from a promoted artifact, and rollback restores the previous artifact set.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.06

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.01: static generator
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:wrangler.json; Web:worker/**; Web:.github/workflows/ci.yml; Web:tooling/cloudflare.ts
Shared resources (follow the owner protocol): RES-web-app-routing (append): The application shell task owns root route registration; each surface adds its own route module and per-origin edge directory.; RES-web-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: WEB.09, WEB.30, WEB.31

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Cloud-outage independence test, atomic deployment test, rollback test — offline/local against the real Cloudflare account under existing CI secrets
Completion evidence for the ledger: A full cloud outage leaves the site fully available; deployment is atomic; rollback restores the previous set
```

```text
Execute ArcForges delivery task WEB.08 — Owned consumer design system (packages/ui).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-08 (python tools/delivery.py claim WEB.08 --worker <name>); task branch task/web-08 in Web; ledger record ledger/tasks/web-08.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: packages/ui grows from a placeholder Shell/Button into a full design-token system (typography, spacing, color, themes), owned accessible primitives, a test-only component catalogue, approved visual baselines and reusable account/usage/chat primitives, with localization/long-label/mobile-nav/focus/reduced-motion/loading-error-empty variants.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.07

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.03: Node/npm workspace
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:packages/ui/**
Shared resources (follow the owner protocol): RES-web-shared-ui (append): The design-system task owns the shared UI package; surfaces request components through it; additions after it are additive.
Unblocks: WEB.09, WEB.10, WEB.19

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): React Testing Library behavior tests; production-rendered Playwright visual snapshots for representative viewport/theme/locale combinations (local opt-in per playwright.config.ts's CI guard); automated accessibility and dated human visual/keyboard review; dependency/licence/provenance checks
Completion evidence for the ledger: Approved consumer layouts and complete accessible states
Notes: Has NO dependency on WEB.01-WEB.07 (different package, only needs WP02 which is already satisfied) and should be started in parallel with the site generator work, not after it — it is the critical-path input for both WEB.10 (account) and WEB.19 (chat).
```

```text
Execute ArcForges delivery task WEB.09 — Verify the owned Site artifact and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-09 (python tools/delivery.py claim WEB.09 --worker <name>); task branch task/web-09 in Web; ledger record ledger/tasks/web-09.md.
Kind/size: integration/S. Baseline: not-started.
Outcome: The React-generated static Site with localization/SEO and no production Node server is verified end to end; independently published product/version/download metadata is consumed through the fixed release contract, with pending later owners and their closing gates recorded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-47.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\47-static-public-site.md, anchor rule-wp-47.90
- WP-47:browser-matrix-acceptance-paragraph-brow Browser matrix acceptance paragraph (browser-support.v1 for the static site output) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\47-static-public-site.md, package-level obligation

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

Permitted write scope: Web:apps/site/**
Unblocks: REL.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Static/no-script/accessibility/link and artifact-version checks; private candidate download fixtures labelled; public promotion waits for WP50
Completion evidence for the ledger: Owned-artifact-and-real-integration receipt including browser-support.v1 evidence for the site output
Notes: Provides the tooling WP45's operations console needs ("47 tooling must precede 45" per producer-artifacts-and-integration.md); the commerce, policy and operations lanes should reference this task's 'web-static-generator'/'web-design-system' tokens as its own start need rather than waiting on all of WP47's numeral position in the old serial plan.
```

```text
Execute ArcForges delivery task WEB.10 — Account shell: route graph, deployment-profile selection, generated-SDK wiring.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-10 (python tools/delivery.py claim WEB.10 --worker <name>); task branch task/web-10 in Web; ledger record ledger/tasks/web-10.md.
Kind/size: producer/XL. Baseline: not-started.
Outcome: The apps/app workspace member is created with the account deployment profile: route graph/shell composed from packages/ui + generated TS SDK + TanStack Query, Android callback/assetlinks wiring, responsive overview/navigation, safe public runtime config, error boundaries, and loading/empty/pending/expired states with cache-clear-and-abort on user/workspace change.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.00

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.08: design system tokens/components
- [contract] CON.07: generated TS SDK (@arcforges/api-client/@arcforges/proto)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.12: identity/browser/native endpoints

Permitted write scope: Web:apps/app/**; Web:package.json
Shared resources (follow the owner protocol): RES-contract-consumer-pins (append): A consumer task updates the pin it needs through a reviewed dependency change to the exact published candidate containing its closure; no consumer pins an unpublished closure or references Contracts source.; RES-web-app-routing (append): The application shell task owns root route registration; each surface adds its own route module and per-origin edge directory.; RES-web-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-web-shared-ui (append): The design-system task owns the shared UI package; surfaces request components through it; additions after it are additive.
Unblocks: WEB.11, WEB.13, WEB.14, WEB.15, WEB.16, WEB.19

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): TypeScript/RTL checks; no-cookie-leakage/state/PKCE/origin-mismatch and Android-verified-links tests; production route/chunk isolation, both themes, keyboard/narrow layouts — fixture-backed CI plus local opt-in real-browser evidence
Completion evidence for the ledger: Profile isolation and composition results
```

```text
Execute ArcForges delivery task WEB.11 — Real browser session and step-up acceptance.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-11 (python tools/delivery.py claim WEB.11 --worker <name>); task branch task/web-11 in Web; ledger record ledger/tasks/web-11.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Passkey/email verification/recovery, live opaque cookie session, server-controlled expiry/revocation and sensitive-action step-up work on the real account origin topology; no bearer/refresh token ever enters the app.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.01

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.19: the P2-003 same-origin cookie-session adapter
- [artifact] WEB.10: account shell
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:apps/app/app/features/account/**
Unblocks: WEB.12, WEB.18

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Playwright against production assets/edge/real Cloud and D1 is local opt-in (login/logout, two origins/tabs, sibling-origin CSRF, passkey expected origin, replica restart, expiry/revoke races); manual passkey/browser matrix supplements automation
Completion evidence for the ledger: Token storage, refresh, step-up and new-browser trust results
```

```text
Execute ArcForges delivery task WEB.12 — Account and security surfaces.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-12 (python tools/delivery.py claim WEB.12 --worker <name>); task branch task/web-12 in Web; ledger record ledger/tasks/web-12.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Profile, authentication methods, passkey management, sessions, device list with trust/revocation, recovery configuration and the security-event view are complete, with step-up required on every sensitive action.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.02

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.11: session/step-up
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:apps/app/app/features/account/**
Unblocks: WEB.17, WEB.18

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Device-revocation-propagation, passkey add/remove, security-event-visibility and step-up-required-per-action tests — fixture CI plus local opt-in real-Cloud evidence
Completion evidence for the ledger: Device revocation, passkey and step-up coverage results
```

```text
Execute ArcForges delivery task WEB.13 — Workspace, storage and usage.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-13 (python tools/delivery.py claim WEB.13 --worker <name>); task branch task/web-13 in Web; ledger record ledger/tasks/web-13.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Single-owner workspace settings (no membership/invitation/role/seat surface), service-term/included-capacity display with recovery timing and extra-credit opt-in, storage from committed objects, usage-against-quota with visible reset boundaries, and data-health visibility.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.03

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.10: account shell
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.42: R2/committed-object accounting
- [integration] CLOUD.52: data-health status projection (read-only surface only)

Permitted write scope: Web:apps/app/app/features/workspace/**
Unblocks: WEB.17, WEB.18

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Accounting comparison against server-side figures; structural test asserting no membership/invitation/role/seat operation; projection test asserting no supplier rate/route-weight leakage; capacity-vs-credits never-summed display test
Completion evidence for the ledger: Storage and usage accounting comparison
```

```text
Execute ArcForges delivery task WEB.14 — Subscription, capacity, credits and hosted checkout.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-14 (python tools/delivery.py claim WEB.14 --worker <name>); task branch task/web-14 in Web; ledger record ledger/tasks/web-14.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Consumer subscription/management views use public server projections and generated operations; paid-term state, replenishing capacity and purchased credits display separately; hosted checkout opens in-browser and shows confirming until verified Cloud state changes; no client/provider redirect grants entitlement.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.04 (all work except the parts mapped to WEB.29): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.04

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.10: account shell
- [contract] CON.08: commerce/entitlement wire records
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] COM.14: real commerce ledger/test-mode checkout environment
- [integration] POL.02: real policy projections for rate-limit/recovery reasons

Permitted write scope: Web:apps/app/app/features/commerce/**
Unblocks: WEB.17, WEB.18, WEB.29, WEB.30, WEB.31

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Real C# accounting/checkout-test-environment flows; exact-amount display above JS safe-integer boundaries; duplicate-click/cancelled/failed/late-confirmation/refund/term-expiry/stale-price tests — local opt-in against a real test-mode provider
Completion evidence for the ledger: Entitlement reason coverage, credit separation and no-payment-field scan
```

```text
Execute ArcForges delivery task WEB.15 — Data export and deletion.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-15 (python tools/delivery.py claim WEB.15 --worker <name>); task branch task/web-15 in Web; ledger record ledger/tasks/web-15.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Export requests show progress and download; deletion requests show a grace period and an explicit, accurate statement of what is and is not deleted, including that local data is untouched.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.05

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.10: account shell
- [contract] CON.22: published data and export operations
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.45: real export job mechanics

Permitted write scope: Web:apps/app/app/features/data/**
Unblocks: WEB.17, WEB.18

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Export-completeness, deletion-statement-accuracy, grace-period and local-data-assertion tests
Completion evidence for the ledger: Export completeness and deletion statement accuracy
```

```text
Execute ArcForges delivery task WEB.16 — Origin security and performance (account).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-16).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-16 (python tools/delivery.py claim WEB.16 --worker <name>); task branch task/web-16 in Web; ledger record ledger/tasks/web-16.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: A strict CSP with no default inline script, per-origin cookie/CORS/CSRF posture, no secret in the bundle, sandboxed preview of user content, and bundle-size/first-interactive budgets with regression gates.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.06

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.10: account shell
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:deploy/edge/account/**
Shared resources (follow the owner protocol): RES-web-app-routing (append): The application shell task owns root route registration; each surface adds its own route module and per-origin edge directory.; RES-web-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: WEB.18

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Policy header verification; bundle secret scan; sandbox escape test on hostile content; budget measurements with regression gate — offline/CI-eligible
Completion evidence for the ledger: Policy headers, bundle secret scan and budget measurements
```

```text
Execute ArcForges delivery task WEB.17 — Offline, degradation and accessibility (account).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-17).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-17 (python tools/delivery.py claim WEB.17 --worker <name>); task branch task/web-17 in Web; ledger record ledger/tasks/web-17.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Honest offline behaviour preserving unsent input, a cloud-outage state naming unavailable capabilities with reasons rather than blanking, and full keyboard-only accessibility on every major workflow.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.07

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.12: account/security surfaces
- [artifact] WEB.13: workspace/storage surfaces
- [artifact] WEB.14: commerce surfaces
- [artifact] WEB.15: data surfaces
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:apps/app/**; Web:tests/**
Unblocks: WEB.18

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline-behaviour tests; cloud-outage-no-blank test; accessibility automated and manual passes
Completion evidence for the ledger: Offline, outage and accessibility results
```

```text
Execute ArcForges delivery task WEB.18 — Verify the owned Account artifact and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-18).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-18 (python tools/delivery.py claim WEB.18 --worker <name>); task branch task/web-18 in Web; ledger record ledger/tasks/web-18.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Real browser evidence against the AOT release closes cookie secrecy, CSRF, expiry/revocation, privacy/export and admission/usage display; the account deployment profile is the sole account application with no AGPL import into Mobile.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.90 (full; final-review closure: 08-security-architecture account/provider closure, scoped-token display-once, cancellation restricted route): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.90
- WP-48:required-implementation-and-closure-from Required implementation and closure from the final review: 08-security-architecture account/provider closure, scoped-token display-once, cancellation restricted route (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\48-account-portal.md, package-level obligation
- WP-48:browser-matrix-acceptance-paragraph-brow Browser matrix acceptance paragraph (browser-support.v1 for the account output) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\48-account-portal.md, package-level obligation

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

Permitted write scope: Web:apps/app/**
Unblocks: REL.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Real browser against the AOT release: cookie secrecy, CSRF, expiry/revocation, privacy/export and admission/usage display — local opt-in per P2-017
Completion evidence for the ledger: Owned-artifact-and-real-integration receipt; contributes its scoped evidence toward PG-23 (closed later at WP50, not here)
```

```text
Execute ArcForges delivery task WEB.19 — Chat shell: route composition and design-system integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-19).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-19 (python tools/delivery.py claim WEB.19 --worker <name>); task branch task/web-19 in Web; ledger record ledger/tasks/web-19.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Chat routes are composed in the same ArcForges.Web.App codebase using owned UI tokens/components and the generated TS SDK; Account/Chat assets, cookies, query scopes and public config are independently selected and validated; responsive conversation navigation/composer/task panel and native-product handoff work with keyboard/reduced-motion support.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.00

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.08: design system tokens/components
- [artifact] WEB.10: account shell and apps/app workspace registration
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:apps/app/app/features/chat/**
Shared resources (follow the owner protocol): RES-web-app-routing (append): The application shell task owns root route registration; each surface adds its own route module and per-origin edge directory.; RES-web-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-web-shared-ui (append): The design-system task owns the shared UI package; surfaces request components through it; additions after it are additive.
Unblocks: WEB.20, WEB.21, WEB.22, WEB.23, WEB.25, WEB.30, WEB.31

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Production route/profile inspection; approved light/dark/narrow-screen visual baselines; keyboard/touch/long-text states; source/dependency assertion that no provider or Harness implementation enters the browser
Completion evidence for the ledger: Cross-profile isolation results
```

```text
Execute ArcForges delivery task WEB.20 — Conversation and generated output streams.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-20).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-20 (python tools/delivery.py claim WEB.20 --worker <name>); task branch task/web-20 in Web; ledger record ledger/tasks/web-20.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: The full Chat UI uses annex-10 gRPC-Web binary output/event streams with durable recovery; Cloud history is authoritative except memory-only temporary UI; an interrupted stream is always shown as interrupted, never complete.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.01 (all work except the parts mapped to WEB.27): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.01

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.19: chat shell + real deployed WP23/24 transport (inherited via WEB.10)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] WEB.27: real CF Harness admission/generation/tool loop

Permitted write scope: Web:apps/app/app/features/chat/**; Web:tests/chat/**
Permitted substitutes (never real integration evidence): SUB-fixture-turn-endpoint: client-side session/event/output/upload handling, typed state transitions, reconnection -- runs no model/planner/admission/metering itself Real producer ['HAR.00', 'HAR.02', 'HAR.03']; removed by HAR.05
Unblocks: WEB.24, WEB.26, WEB.27

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Generated event-contract and recovery tests (byte offsets, reconnect/gaps, duplicate delivery, loss of authorization); browser-support.v1 polling-fallback behavior (EventService.Poll every 10s +/-20% jitter, ExecutionService.ReadOutput every 5s after the 45s stream-silence timeout)
Completion evidence for the ledger: Streaming, interruption and partial-message results
```

```text
Execute ArcForges delivery task WEB.21 — Tasks, approval and steering.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-21).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-21 (python tools/delivery.py claim WEB.21 --worker <name>); task branch task/web-21 in Web; ledger record ledger/tasks/web-21.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Task/run/step/tool-call surfaces with progress; approve/reject/cancel/pause/retry/steer as idempotent commands; local-presence-required operations are clearly refused with an explanation; no missed notification loses a pending approval.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.02 (all work except the parts mapped to WEB.27, WEB.28): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.02

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.19: chat shell
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] WEB.28: real device bridge
- [integration] WEB.27: real Harness planning/tool-proposal loop

Permitted write scope: Web:apps/app/app/features/tasks/**; Web:tests/chat/**
Unblocks: WEB.24, WEB.26, WEB.27, WEB.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Idempotency-per-control, local-presence-negative, approval-expiry and durable-attention tests
Completion evidence for the ledger: Control idempotency, local-presence and attention-durability results
```

```text
Execute ArcForges delivery task WEB.22 — Artifacts and sandboxing.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-22).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-22 (python tools/delivery.py claim WEB.22 --worker <name>); task branch task/web-22 in Web; ledger record ledger/tasks/web-22.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Artifact preview runs inside an isolated sandbox so untrusted content never executes in the application origin; downloads verify permission at access; no public share links exist in V1.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.03

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.19: chat shell
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:apps/app/app/features/artifacts/**
Unblocks: WEB.24, WEB.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Sandbox-escape attempt with hostile content; permission-at-access test; existence-disclosure test on a denied resource; public-share-link absence assertion
Completion evidence for the ledger: Sandbox escape, permission-at-access and share-link absence results
Notes: Self-contained: mostly a client-side iframe/CSP isolation mechanism plus WP25 resource tickets already inherited via the account shell; does not need WP26 or WP52.
```

```text
Execute ArcForges delivery task WEB.23 — One-application remote control.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-23).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-23 (python tools/delivery.py claim WEB.23 --worker <name>); task branch task/web-23 in Web; ledger record ledger/tasks/web-23.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Device applications are listed, an explicit authorized product/installation is selected and frozen per task target; no browser local connection, another-product tool or local-only desktop chat access exists; an offline target shows an honest queued state with expiry.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.04 (all work except the parts mapped to WEB.28): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.04

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.19: chat shell + real device-presence API (inherited)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] WEB.28: real device bridge dispatch

Permitted write scope: Web:apps/app/app/features/devices/**
Unblocks: WEB.24, WEB.26, WEB.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Scope/permission, wrong-or-stale-target, loss/retry and expiry scenarios against the exact real artifact/owner boundary
Completion evidence for the ledger: Offline-target queueing and no-local-connection results
```

```text
Execute ArcForges delivery task WEB.24 — Offline, degradation and accessibility (chat).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-24).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-24 (python tools/delivery.py claim WEB.24 --worker <name>); task branch task/web-24 in Web; ledger record ledger/tasks/web-24.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Honest offline messaging preserving unsent input; realtime loss degrades to polling with backfill; a cloud outage reports unavailable capabilities rather than blanking; every core workflow completes by keyboard.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.05

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.20: streaming UI
- [artifact] WEB.21: tasks UI
- [artifact] WEB.22: artifacts UI
- [artifact] WEB.23: device UI
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:apps/app/**; Web:tests/chat/**
Unblocks: WEB.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/reconnection tests; polling-degradation test; cloud-outage test; accessibility automated and manual passes
Completion evidence for the ledger: Offline, degradation, convergence and accessibility results
```

```text
Execute ArcForges delivery task WEB.25 — Performance budgets (chat).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-25).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-25 (python tools/delivery.py claim WEB.25 --worker <name>); task branch task/web-25 in Web; ledger record ledger/tasks/web-25.md.
Kind/size: feature/S. Baseline: not-started.
Outcome: Bundle size, first-interactive and interaction-responsiveness budgets are measured per release candidate with a regression gate that catches a deliberate regression.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.06

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.19: chat shell
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:apps/app/app/features/chat/**
Shared resources (follow the owner protocol): RES-web-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: WEB.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Budget measurements per release candidate; regression-gate negative test
Completion evidence for the ledger: Budget measurements and regression-gate negative test
```

```text
Execute ArcForges delivery task WEB.26 — Verify the owned Chat artifact and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-26).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-26 (python tools/delivery.py claim WEB.26 --worker <name>); task branch task/web-26 in Web; ledger record ledger/tasks/web-26.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: A full real admitted CF turn/tool/approval/reconnect sequence is exercised in a browser using the fixed same-origin session and generated AI gRPC-Web route; a blocked/expired live stream reconciles to the authoritative result without leaking session credentials.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.90
- WP-49:browser-matrix-acceptance-paragraph-brow Browser matrix acceptance paragraph (browser-support.v1 for the chat output) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\49-arcchat-web-companion.md, package-level obligation

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.20: streaming
- [artifact] WEB.21: tasks/approval
- [artifact] WEB.22: artifacts
- [artifact] WEB.23: remote control
- [artifact] WEB.24: resilience
- [artifact] WEB.25: budgets
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] WEB.27: real Harness

Permitted write scope: Web:apps/app/**
Unblocks: REL.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Full real admitted CF turn/tool/approval/reconnect in a browser — local opt-in per P2-017
Completion evidence for the ledger: Owned-artifact-and-real-integration receipt; contributes its scoped evidence toward PG-23 (closed later at WP50)
```

```text
Execute ArcForges delivery task WEB.27 — Real CF Harness generation/tool loop observed end to end in the browser.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-27).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-27 (python tools/delivery.py claim WEB.27 --worker <name>); task branch task/web-27 in Web; ledger record ledger/tasks/web-27.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: real admitted generation and tool proposal replace the contract-bound fixture turn endpoint in Chat

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.01 (real-integration closure): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.01
- WP-49.02 (real-integration closure): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.02

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
```

```text
Execute ArcForges delivery task WEB.28 — Real desktop tool dispatch from the browser companion.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-28).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-28 (python tools/delivery.py claim WEB.28 --worker <name>); task branch task/web-28 in Web; ledger record ledger/tasks/web-28.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: a browser-initiated remote task actually reaches a desktop through the durable bridge

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-49.02 (device-dispatch closure): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.02
- WP-49.04 (real-integration closure): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\49-arcchat-web-companion.md, anchor rule-wp-49.04

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
```

```text
Execute ArcForges delivery task WEB.29 — Real commerce/policy provider evidence for the account portal.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-29).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/web-29 (python tools/delivery.py claim WEB.29 --worker <name>); task branch task/web-29 in Web; ledger record ledger/tasks/web-29.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: hosted checkout, entitlement reasons and rate-limit/recovery text reflect a real test-mode ledger and policy service, not contract fixtures

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-48.04 (real-provider-evidence closure): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\48-account-portal.md, anchor rule-wp-48.04

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
```

```text
Execute ArcForges delivery task WEB.30 — Real React Web client against deployed browser session/PublicApi/realtime.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-30).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web). Also touches: Cloud.
Claim and handoff record: claims/web-30 (python tools/delivery.py claim WEB.30 --worker <name>); task branch task/web-30 in Web; ledger record ledger/tasks/web-30.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Real TS gRPC-Web client, cookie/CSRF/Origin session behavior and realtime streams against the deployed Cloud, beyond MSW fixtures

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.05 (Web real-consumer integration): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.05

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.19: real, delivered outcome of CLOUD.19 (Browser cookie-session adapter and full account-surface closure)
- [artifact] CLOUD.26: real, delivered outcome of CLOUD.26 (Generated C#/TypeScript/Kotlin clients against Identity/Workspace/Device)
- [artifact] CLOUD.29: real, delivered outcome of CLOUD.29 (Stream connection and authentication (EventService.Watch/ExecutionService.WatchOutput shells))
- [artifact] WEB.07: real, delivered outcome of WEB.07 (Independence and atomic deployment)
- [artifact] WEB.14: real, delivered outcome of WEB.14 (Subscription, capacity, credits and hosted checkout)
- [artifact] WEB.19: real, delivered outcome of WEB.19 (Chat shell: route composition and design-system integration)
- [artifact] PRF.08: React production build and generated SDK proof using MSW fixtures
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: CLOUD.28, WEB.31

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: Real TS gRPC-Web client, cookie/CSRF/Origin session behavior and realtime streams against the deployed Cloud, beyond MSW fixtures
```

```text
Execute ArcForges delivery task WEB.31 — Full browser-support.v1 matrix across all Web-facing outputs.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\web.md (anchor task-web-31).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web). Also touches: Cloud.
Claim and handoff record: claims/web-31 (python tools/delivery.py claim WEB.31 --worker <name>); task branch task/web-31 in Web; ledger record ledger/tasks/web-31.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Supported/degraded/blocked behavior across every output's flows on real browser/OS patches; WP-50 joins all production hashes and real browser evidence

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23:browser-matrix-acceptance-appendix-full Browser matrix acceptance appendix, full cross-area join (Browser matrix acceptance appendix, full cross-area join): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\23-public-api-and-generated-clients.md, package-level obligation

Entry condition: adoption slice ADOPT.09.web is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] OPS.05: real, delivered outcome of OPS.05 (Operator console and support access)
- [artifact] WEB.07: real, delivered outcome of WEB.07 (Independence and atomic deployment)
- [artifact] WEB.14: real, delivered outcome of WEB.14 (Subscription, capacity, credits and hosted checkout)
- [artifact] WEB.19: real, delivered outcome of WEB.19 (Chat shell: route composition and design-system integration)
- [artifact] WEB.30: the real React Web client against the deployed browser session
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.28: the WP-23 browser-matrix Cloud part accepted

Permitted write scope: 

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: Supported/degraded/blocked behavior across every output's flows on real browser/OS patches; WP-50 joins all production hashes and real browser evidence
```
