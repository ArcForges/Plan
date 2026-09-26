# ArcForges delivery task prompts — Desktop distribution and update

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Desktop distribution and update

```text
Execute ArcForges delivery task UPD.01 — Signed feed and applicable-target selection.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\updater.md (anchor task-upd-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/upd-01 (python tools/delivery.py claim UPD.01 --worker <name>); task branch task/upd-01 in DesktopPlatform; ledger record ledger/tasks/upd-01.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: update.feed.v1 canonical JSON envelope validation, trust (ECDSA P256/SHA256 over RFC8785-canonical payload), product/RID/channel selection, compatibility and anti-replay per architecture 14 SS8.1; only an admitted target from a current trusted feed can enter download.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-53.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\53-desktop-distribution-and-update.md, anchor rule-wp-53.00

Entry condition: adoption slice ADOPT.02.updater is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.40: secure key-handling/signature-verification patterns from Security
- [artifact] FND.05: reason-code registry
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Update/ArcForges.Update/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Permitted substitutes (never real integration evidence): SUB-test-signed-update-feed: feed parsing, trust-chain verification, product/RID/channel/version selection and anti-replay mechanics only Real producer ['UPD.07']; removed by REL.10
Unblocks: REL.10, UPD.02, UPD.05, UPD.07, UPD.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: unsigned/expired/duplicate/hash-invalid feed, removed and policy-blocked version independently, wrong product/RID, older signed feed - all against a test-signed fixture feed, no live update.feed.v1 server.
Completion evidence for the ledger: Signed feed schema, replay and blocked-version cases.
```

```text
Execute ArcForges delivery task UPD.02 — Background download and staging.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\updater.md (anchor task-upd-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/upd-02 (python tools/delivery.py claim UPD.02 --worker <name>); task branch task/upd-02 in DesktopPlatform; ledger record ledger/tasks/upd-02.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Background check, range resume, delta reconstruct with verified full fallback, bounded staging and final hash/signature checks; a complete verified candidate is staged without changing the active installation.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-53.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\53-desktop-distribution-and-update.md, anchor rule-wp-53.01

Entry condition: adoption slice ADOPT.02.updater is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] UPD.01: signed feed/target selection
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Update/ArcForges.Update/**
Unblocks: UPD.03, UPD.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: interrupt every transfer boundary, tamper base/delta/target, storage exhaustion - against a local test HTTP fixture server, not a live download surface; launch-remains-available assertion.
Completion evidence for the ledger: Actual resumed download, delta/full reconstruction and tamper refusal.
```

```text
Execute ArcForges delivery task UPD.03 — Safe apply and atomic activation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\updater.md (anchor task-upd-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/upd-03 (python tools/delivery.py claim UPD.03 --worker <name>); task branch task/upd-03 in DesktopPlatform; ledger record ledger/tasks/upd-03.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: The real lifecycle shutdown handshake (await all affected instances exiting without holding domain locks) plus the selected Velopack adapter drive download->verify->stage->atomic-switch->retain-previous-launchable-version; busy work defers apply; restart sees either the previous or the new verified installation, never a partial one.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-53.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\53-desktop-distribution-and-update.md, anchor rule-wp-53.02

Entry condition: adoption slice ADOPT.02.updater is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] UPD.02: staged verified candidate
- [artifact] PLT.32: lifecycle/shutdown handshake (WP-10.06)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Update/ArcForges.Update/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: UPD.04, UPD.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/local tests: long render/capture, unsaved edit, peer unavailable, canceled restart and kill at each activation boundary - simulated process-level, not a real installed multi-instance product (that is UPD.08's job).
Completion evidence for the ledger: Busy/unsaved work deferral and interrupted apply.
```

```text
Execute ArcForges delivery task UPD.04 — Rollback and migration interlock.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\updater.md (anchor task-upd-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/upd-04 (python tools/delivery.py claim UPD.04 --worker <name>); task branch task/upd-04 in DesktopPlatform; ledger record ledger/tasks/upd-04.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: The update journal is persisted outside install/data files; uses the existing data-store migration read/write compatibility horizon before rollback; user data survives; an incompatible automatic rollback refuses with a recovery reason instead of opening data with the old binary.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-53.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\53-desktop-distribution-and-update.md, anchor rule-wp-53.03
- WP-53:versioned-installation-update-journal-pe Versioned installation update journal persisted outside install/data files; the updater never writes product data or implements schema migration (SS6 impacts, BR-05) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\53-desktop-distribution-and-update.md, package-level obligation

Entry condition: adoption slice ADOPT.02.updater is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] UPD.03: safe apply/activation
- [artifact] PLT.04: migration runner's read/write compatibility-horizon concept (WP-07.03)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Update/ArcForges.Update/**
Unblocks: UPD.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: fail pre-migration startup, fail during migration, current store outside previous reader/writer horizon, interrupted rollback.
Completion evidence for the ledger: Compatible rollback, incompatible migration refusal and launch recovery.
```

```text
Execute ArcForges delivery task UPD.05 — Channels, staged rollout and security updates.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\updater.md (anchor task-upd-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/upd-05 (python tools/delivery.py claim UPD.05 --worker <name>); task branch task/upd-05 in DesktopPlatform; ledger record ledger/tasks/upd-05.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Explicit channel selection, stable installation-based rollout assignment, halting bad versions and respecting minimum-version grace, using activated WP-44 policy and the WP-45 advisory process; urgency cannot force unsafe restart.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-53.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\53-desktop-distribution-and-update.md, anchor rule-wp-53.04

Entry condition: adoption slice ADOPT.02.updater is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] UPD.01: signed feed
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] POL.09: real activated Cloud policy distribution and the WP-45 advisory process

Permitted write scope: DesktopPlatform:src/Update/ArcForges.Update/**
Permitted substitutes (never real integration evidence): SUB-updater-policy-fixture: deterministic per-installation rollout assignment stability and channel-switch mechanics against a locally authored fixture policy document Real producer ['POL.09']; removed by UPD.08
Unblocks: UPD.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: both channel directions, unchanged rollout assignment across restart, blocked target after download, emergency offer during critical work, expired grace - all against the fixture policy document above.
Completion evidence for the ledger: Stable rollout, channels and expedited security/grace behavior.
```

```text
Execute ArcForges delivery task UPD.06 — Diagnostics and preserving data on uninstall.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\updater.md (anchor task-upd-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/upd-06 (python tools/delivery.py claim UPD.06 --worker <name>); task branch task/upd-06 in DesktopPlatform; ledger record ledger/tasks/upd-06.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: check/download/verify/stage/apply/defer/fail/rollback recorded with stable reasons and correlation, no user content; uninstall never implicitly removes user data or the recovery journal.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-53.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\53-desktop-distribution-and-update.md, anchor rule-wp-53.05

Entry condition: adoption slice ADOPT.02.updater is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.47: emission/dimension surface (WP-12.00)
- [artifact] FND.05: reason-code registry
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Update/ArcForges.Update/**
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: UPD.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: independent expected activity sequence; uninstall/reinstall preserving product data and recovery journal (simulated file-system scenario).
Completion evidence for the ledger: Update reason-code sequence and data-preserving uninstall.
```

```text
Execute ArcForges delivery task UPD.07 — Production catalog and Android distribution trust.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\updater.md (anchor task-upd-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/upd-07 (python tools/delivery.py claim UPD.07 --worker <name>); task branch task/upd-07 in DesktopPlatform; ledger record ledger/tasks/upd-07.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Production catalog/revocation and Android direct-update feeds using WP03 formats, with signing custody/rotation and artifact URI/certificate inventory; registers per-product desktop auth URI schemes in signed installers.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-53.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\53-desktop-distribution-and-update.md, anchor rule-wp-53.07

Entry condition: adoption slice ADOPT.02.updater is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] UPD.01: signed feed mechanics
- [contract] CON.16: native auth exceptions, catalog/index/revocation/update/realm schemas and independent signed vectors
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Update/ArcForges.Update/**; DesktopPlatform:eng/packaging/**
Unblocks: REL.10, UPD.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: real signatures/shards/monotonic revision, current/previous trust, Android certificate match and desktop callback registration from installed packages - against test key material; production key custody itself is an operational/local-opt-in concern, not a CI-testable behavior.
Completion evidence for the ledger: WP50 can replace WP32/WP41 fixture keys with production feeds without changing schemas.
```

```text
Execute ArcForges delivery task UPD.08 — Publish ArcForges.Update and verify the complete lifecycle.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\updater.md (anchor task-upd-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/upd-08 (python tools/delivery.py claim UPD.08 --worker <name>); task branch task/upd-08 in DesktopPlatform; ledger record ledger/tasks/upd-08.md.
Kind/size: acceptance/M. Baseline: not-started.
Outcome: ArcForges.Update is packed with its verified closure, restored into clean consumer applications, and exercised through a real Tier 1 install->staged update->restart->rollback cycle against a test-signed feed, including interrupted download/apply, blocked versions, signature corruption and wrong data horizon.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-53.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\53-desktop-distribution-and-update.md, anchor rule-wp-53.90

Entry condition: adoption slice ADOPT.02.updater is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] UPD.01: signed feed
- [artifact] UPD.02: download/staging
- [artifact] UPD.03: safe apply
- [artifact] UPD.04: rollback/migration interlock
- [artifact] UPD.05: channels/rollout
- [artifact] UPD.06: diagnostics/uninstall
- [artifact] UPD.07: production catalog/trust
- [artifact] PRF.01: a real signed candidate AOT application to install/update
- [artifact] POL.09: client policy resolution library
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] REL.10: production installers, production domains/signing and the full release matrix

Permitted write scope: DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.
Unblocks: POL.07, REL.01, REL.02, REL.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017: Tier 1 (Windows/Linux) real install/apply/rollback cycle is the kind of local, affected-scope, once, existing-environment runtime check P2-017 permits and expects to be recorded, distinct from hosted CI; Tier 2 (macOS) follows the existing recorded waiver process, never macOS CI.
Completion evidence for the ledger: Owned artifact and real-integration receipt per WP-53.90.
```
