# ArcForges delivery task prompts — ArcNotes

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## ArcNotes

```text
Execute ArcForges delivery task NOTES.01 — Notebook/folder hierarchy, document placement and structural commands.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-01 (python tools/delivery.py claim NOTES.01 --worker <name>); task branch task/notes-01 in ArcNotes; ledger record ledger/tasks/notes-01.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: ArcNotes.Domain has Notebook/Folder/Document aggregates with fractional-ordinal placement, cycle-denial, cross-notebook move and trash/restore, each structural edit a single-write-path transaction producing a typed structural outbox entry (contentProposal|namedStructuralCommand union per data-model 02).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-18.00 (notebook->folder hierarchy, stable folder IDs, document placement, notebook-owned structural commands, no-documents-in-documents; final-review paragraph: typed structural outbox entries, multi-root local tokens, move classification mapping/preview, offline create->move->edit crash test): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.00
- WP-18:final-review-paragraph-s5-before-18-90-i Final-review paragraph (S5, before 18.90): independent verification of 02-desktop-data-model; typed structural outbox entries; multi-root local tokens; complete move classification mapping/preview; offline create->move->edit and crash-before/after-acknowledgement test; scalar-definition fixtures follow the fixed profile (WP-28 repeats with real property/view UI) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, package-level obligation

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.01: published ArcForges.Persistence.Sqlite commit-unit (state+command+journal+revision+outbox in one transaction)
- [contract] CON.91: NotebookView, FolderView, NotesDocument wire records in ArcForges.Contracts.PublicApi
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.37: Cloud canonical Notes schema (notebook-owned folders/documents) accepts the identical structural operations (create/rename/move/reorder/trash/restore) Notes implements locally

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Domain/Notebooks/**; ArcNotes:src/ArcForges.ArcNotes.Domain/Folders/**; ArcNotes:src/ArcForges.ArcNotes.Infrastructure/Migrations/0001_*; ArcNotes:tests/ArcForges.ArcNotes.Tests/Domain/Structural/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcnotes-composition (append): Each feature registers services and capabilities through its own registration module; the composition root only lists modules; ordering conflicts are resolved at merge.; RES-arcnotes-migrations (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: NOTES.06, NOTES.07, NOTES.14, NOTES.19, NOTES.20, NOTES.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests (deep folders, cycle denial, reorder, cross-notebook move, delete/restore, immutable revision references); AOT compile; no live Cloud call in this task's own tests
Completion evidence for the ledger: folder structure/document placement ownership+revision rule test results; structural-command atomicity results; offline create->move->edit crash-recovery result
Notes: Does not need WP-14 (Hub/provider slice) or WP-10 (shell) - this is pure domain+persistence, hostable in a unit-test process before any UI exists.
```

```text
Execute ArcForges delivery task NOTES.02 — Block/inline content model, EditTransaction engine, kind conversions and clipboard.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-02 (python tools/delivery.py claim NOTES.02 --worker <name>); task branch task/notes-02 in ArcNotes; ledger record ledger/tasks/notes-02.md.
Kind/size: feature/XL. Baseline: not-started.
Outcome: A closed Block/InlineContent domain model and EditTransaction operation set (InsertBlock, RemoveBlock, MoveBlock, SetBlockKind, SplitBlock, MergeBlocks, ReplaceInlineRange, ApplyMark, SetBlockAttribute, SetProperty) exist with computed inverses, atomic apply, declared conversion mappings and no markup-string round-trip anywhere on an internal path.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-18.00 (typed inline content model, closed block-kind set, EditTransaction closed operation set with computed inverses and fractional ordinals, declared kind-conversion mappings, multi-block selection, drag/drop move-vs-reference-vs-copy, unknown-kind/mark forward compatibility; clipboard tests: exact code round-trip, table-shape preservation; repository-policy test that no internal path serialises content to Markdown/HTML/RTF): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.00
- WP-18.90 (block/document/editor scalar base and content-origin/attachment checks (domain-model portion)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.90
- WP-18:p2-010-required-behavior-and-closure-bot P2-010 required behavior and closure (bottom of file): stable run/atom/cell IDs, NotesTextPosition/NotesCommand, explicit IME conflict preservation, disabled stale undo with original recoverable inverse, no unspecified rebase (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, package-level obligation
- WP-18:s8-additional-completion-requirement-con S8 additional completion requirement: content paths pass the stated content-origin vectors, including unknown input and failed publication (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, package-level obligation

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.01: same persistence commit-unit as NOTES.01
- [contract] CON.91: Block, BlockBody, BlockProperties, RichText, TextSpan, InlineAtom, LinkSpec, MathContent, TableBlock/TableRow/TableCell wire records
- [contract] CON.03: a published wire schema for the EditTransaction/BlockEdit operation list that architecture/contracts/02-local-rpc-operations.md NO-01 calls 'the typed notes.commands.v1 edit list'
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] NOTES.35: three-device convergence harness exercises Notes block edits end to end

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Domain/Blocks/**; ArcNotes:src/ArcForges.ArcNotes.Domain/Editing/**; ArcNotes:fixtures/formats/arcnotes/v1/**; ArcNotes:tests/ArcForges.ArcNotes.Tests/Domain/Editing/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcnotes-composition (append): Each feature registers services and capabilities through its own registration module; the composition root only lists modules; ordering conflicts are resolved at merge.; RES-arcnotes-format-fixtures (append): Fixtures are added per task under its own subdirectory; manifests are append-only; golden fixtures are never regenerated to pass a test.; RES-arcnotes-migrations (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: NOTES.06, NOTES.08, NOTES.10, NOTES.14, NOTES.15, NOTES.19, NOTES.27, NOTES.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests: command round-trip per block kind, multi-block operation tests, block-identity stability test, transaction-atomicity test, conversion matrix, forward-compatibility test on unknown kinds/marks, clipboard round-trip tests, repository-policy test (no Markdown/HTML/RTF on internal path); AOT compile
Completion evidence for the ledger: write-path/atomicity/conversion-mapping/block-identity-stability results; no-markup-string repository policy test result; per-kind command round-trip and clipboard fidelity results
Notes: Could be further split (block/inline core vs conversion+clipboard) if a single PR proves too large in practice; kept as one task here because the conversion matrix and clipboard both operate over the same closed operation set and block-identity guarantee.
```

```text
Execute ArcForges delivery task NOTES.03 — Editor interaction: caret, selection, IME composition, markdown-friendly input.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-03 (python tools/delivery.py claim NOTES.03 --worker <name>); task branch task/notes-03 in ArcNotes; ledger record ledger/tasks/notes-03.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: The ArcNotes.Desktop editor surface handles grapheme/bidi-correct caret and selection, commits exactly one transaction per IME composition positioned from the real caret rectangle, and supports the closed set of markdown input rules and the slash menu, all built on NOTES.02's EditTransaction model.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-18.01 (grapheme-correct caret/selection, Unicode word boundaries, bidirectional caret movement, discontiguous selection painting, IME composition as view state (one transaction, never interrupted by concurrent edit), markdown keyboard syntax, slash menu distinct from command palette): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.01
- WP-18.00 (P2-010 closure: stable run/atom/cell IDs, NotesTextPosition/NotesCommand, explicit IME conflict preservation, disabled stale undo with original recoverable inverse): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.00
- WP-18:p2-010-required-behavior-and-closure-bot P2-010 required behavior and closure (bottom of file): stable run/atom/cell IDs, NotesTextPosition/NotesCommand, explicit IME conflict preservation, disabled stale undo with original recoverable inverse, no unspecified rebase (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, package-level obligation

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.27: published ArcForges.Desktop.Experience / design-system shell package for Avalonia hosting
- [artifact] APP.01: the independent-product hosting/composition pattern (how ArcNotes.Desktop is composed as its own process under the shared shell)
- [artifact] PLT.26: published design-system tokens and theming
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes/Editor/**; ArcNotes:src/ArcForges.ArcNotes/Editor/Ime/**; ArcNotes:tests/ArcForges.ArcNotes.Tests/Editor/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcnotes-composition (append): Each feature registers services and capabilities through its own registration module; the composition root only lists modules; ordering conflicts are resolved at merge.
Unblocks: NOTES.14, PLT.56

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit/UI-automation tests: text-correctness corpus (emoji with modifiers, Devanagari, Thai, combining marks), composition-input test per platform (one undo entry, one transaction) plus concurrent-edit-during-composition test, bidi caret/selection-painting test; no live device/GUI E2E in CI per P2-017
Completion evidence for the ledger: grapheme/bidi correctness and composition-fidelity results per VF-05/VF-06/VF-07 of 18-editing-and-rich-content.md
```

```text
Execute ArcForges delivery task NOTES.04 — Virtualised block layout, measurement caching and scroll anchoring.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-04 (python tools/delivery.py claim NOTES.04 --worker <name>); task branch task/notes-04 in ArcNotes; ledger record ledger/tasks/notes-04.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: A block layout engine realises only the viewport window plus bounded overscan, caches measurement by (blockId, contentFingerprint, availableWidth, fontScale, locale), and anchors scroll position to (blockId, offset) so a remote edit above the viewport never moves the reader.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-18.01 (virtualised block layout with measurement caching, scroll anchoring to (blockId, offset), bounded nesting, 10000-block scale-corpus responsiveness): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.01

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.26: same design-system/shell package as NOTES.03
- [artifact] PLT.27: the published windows, panels and layout package NOTES.03 also hosts on
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes/Editor/Layout/**; ArcNotes:tests/ArcForges.ArcNotes.Tests/Editor/Layout/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: NOTES.14, NOTES.31

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline scale-corpus benchmark fixture committed to the repo; regressions fail the gate per PF-01/PF-02; no live GUI E2E in CI
Completion evidence for the ledger: 10000-block open-interactive-without-full-measurement result; no-re-measurement-on-scroll-back result; scroll-anchor-above-viewport result
Notes: Split out of WP-18.01 from NOTES.03/05 because layout/virtualisation is a distinct performance-engineering skill area that can proceed in parallel once NOTES.02's block model exists, independent of caret/IME work.
```

```text
Execute ArcForges delivery task NOTES.05 — Rich content kinds: code highlighting, math rendering (notes.math.v1), table interaction.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-05 (python tools/delivery.py claim NOTES.05 --worker <name>); task branch task/notes-05 in ArcNotes; ledger record ledger/tasks/notes-05.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Code blocks highlight from a bounded, statically registered grammar set with graceful plain-text degradation; math blocks render the notes.math.v1 supported grammar subset with an explicit unsupported-construct marker and never execute TeX; table blocks support the interaction set (insert/delete row/column, merge/split-free V1 spans).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-18.01 (code highlighting from a bounded statically-registered grammar set degrading to plain text; math rendering with explicit unsupported-construct marking; run every notes.math.v1 accepted/unsupported/malformed/depth/length vector): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.01

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.27: same shell package as NOTES.03/04
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes/Editor/RichContent/**; ArcNotes:tests/ArcForges.ArcNotes.Tests/Editor/RichContent/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: NOTES.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests running every notes.math.v1 accepted/unsupported/malformed/depth/length vector from 26-product-behavior-profiles.md; code-highlighting degrades off-UI-thread; no live GUI E2E
Completion evidence for the ledger: unsupported-math-construct-renders-as-source-with-marker result; code-block plain-text-degradation result; table-shape clipboard round-trip cross-check with NOTES.02
```

```text
Execute ArcForges delivery task NOTES.06 — Links, backlinks and outline over the canonical block store.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-06 (python tools/delivery.py claim NOTES.06 --worker <name>); task branch task/notes-06 in ArcNotes; ledger record ledger/tasks/notes-06.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Document and block links target stable identities with optional alias; a derived link_index produces the backlinks panel and outline; renaming never breaks a link; a broken link has an explicit state.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-18.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.02

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.01: notebook/document identity
- [artifact] NOTES.02: Block/BlockId model
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Domain/Links/**; ArcNotes:tests/ArcForges.ArcNotes.Tests/Domain/Links/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcnotes-composition (append): Each feature registers services and capabilities through its own registration module; the composition root only lists modules; ordering conflicts are resolved at merge.
Unblocks: NOTES.14, NOTES.19

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests: rename-preserves-link, index rebuild from scratch, broken-link state test, structural test asserting backlinks absent from stored content
Completion evidence for the ledger: link/backlink/index-rebuild results per WP-18.02 completion gate
```

```text
Execute ArcForges delivery task NOTES.07 — Document-level typed properties and tags (basic).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-07 (python tools/delivery.py claim NOTES.07 --worker <name>); task branch task/notes-07 in ArcNotes; ledger record ledger/tasks/notes-07.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: System/user property separation, missing/empty/false/zero distinction, decimal/date/offset validation, label rename vs refused dependent type change, tag cross-cutting classification whose deletion never deletes documents, and plain notes with zero property overhead.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-18.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.03
- WP-18:s8-additional-completion-requirement-pro S8 additional completion requirement: property types and persistence agree with the frozen query profile; no local culture defaults affect stored meaning (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, package-level obligation

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.01: Document aggregate
- [contract] CON.91: PropertyDefinition, PropertyValue, ScalarValue, SelectOption wire records and their constraint sidecars (constraints.json rules propertyDefinition/scalarValue)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Domain/Properties/**; ArcNotes:src/ArcForges.ArcNotes.Domain/Tags/**; ArcNotes:tests/ArcForges.ArcNotes.Tests/Domain/Properties/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcnotes-composition (append): Each feature registers services and capabilities through its own registration module; the composition root only lists modules; ordering conflicts are resolved at merge.; RES-arcnotes-migrations (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: NOTES.14, NOTES.16, NOTES.18, NOTES.23

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests: type validation per property kind, tag-deletion-survives-documents test, default-experience (no-properties) test
Completion evidence for the ledger: property typing and tag-deletion results per WP-18.03 completion gate
Notes: This is the basic document-level property model only; the full typed query/view package (8 scalar kinds incl. relation/derived exclusion, notes.scalar.v1 query evaluator) is WP-28, tasks NOTES.23/24.
```

```text
Execute ArcForges delivery task NOTES.08 — Managed and external attachments (non-PDF): storage, availability, preview levels 1-2.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-08 (python tools/delivery.py claim NOTES.08 --worker <name>); task branch task/notes-08 in ArcNotes; ledger record ledger/tasks/notes-08.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Managed attachments enter the managed resource store with content-hash identity; external references record location+availability; small drags default to managed, large/external prompt; image preview decodes off-thread bounded with EXIF applied; every preview degradation states its reason; no preview path performs a network fetch.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-18.04 (managed/external attachment classification, availability states, metadata-card and thin-preview levels for images/files, bounded off-thread image decode with EXIF orientation, no-embedding structural test, malformed-input degradation for images, egress test (no preview path fetches a remote resource)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.04
- WP-18:s8-additional-completion-requirement-con S8 additional completion requirement: content paths pass the stated content-origin vectors, including unknown input and failed publication (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, package-level obligation

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.05: managed_resource / resource_reference tables (content-addressed blob store) from the persistence foundation
- [artifact] NOTES.02: attachment block kind (image/attachment BlockBody variants)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Infrastructure/Attachments/**; ArcNotes:tests/ArcForges.ArcNotes.Tests/Attachments/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcnotes-composition (append): Each feature registers services and capabilities through its own registration module; the composition root only lists modules; ordering conflicts are resolved at merge.
Unblocks: NOTES.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests: managed round-trip with integrity, reference-unavailable behaviour, malformed-image corpus asserting placeholder+reason+no crash, egress test
Completion evidence for the ledger: attachment integrity, no-embedding, malformed-input degradation and preview-egress results (image/file portion only; PDF portion is NOTES.09)
Notes: Deliberately split from the PDF viewer (NOTES.09) so ordinary attachment handling does not wait on the native PDFium wrapper, which does not exist yet anywhere in DesktopPlatform - this is the aggregate-producer-gate pattern the delivery model avoids.
```

```text
Execute ArcForges delivery task NOTES.09 — PDF in-product viewer, page anchors and native parser isolation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-09 (python tools/delivery.py claim NOTES.09 --worker <name>); task branch task/notes-09 in ArcNotes; ledger record ledger/tasks/notes-09.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: PDF attachments render through the in-product viewer with (attachmentContentHash, pageIndex, rectOrTextRange) page anchors, all parsing routed through ContentSandbox, and a real native-parser-crash test proving the parent process survives with a metadata-card fallback.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-18.04 (PDF viewer (pdfViewer attachment presentation), page-anchored annotation targets, citation anchors, routing hostile PDF parsing through WP-11.09 ContentSandbox, PG-12 completion, PDF-specific malformed-input containment): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.04

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.45: the restricted fixture-parser ContentSandbox runtime (host, protocol, launch mechanics)
- [artifact] NAT.06: the functional native ABI 1.1 (architecture/contracts/06-native-functional-abi.md) that DesktopPlatform's Native.* wrappers implement
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] NAT.14: a real, packaged ArcForges.Native.Pdf (PDFium) wrapper with build/licence inventory and hostile-input containment evidence, equivalent to the 13.13 production-parser-composition step described for ContentSandbox

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Infrastructure/Attachments/Pdf/**; ArcNotes:tests/ArcForges.ArcNotes.Tests/Attachments/Pdf/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Permitted substitutes (never real integration evidence): SUB-notes-pdf-fixture-parser: viewer UI, page-anchor model, preview-degradation logic and sandbox call plumbing only - not real PDFium behaviour Real producer ['NAT.14']; removed by NOTES.37
Unblocks: NOTES.14, NOTES.37

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests against the fixture parser now; real hostile-input containment test deferred to IM.notes-pdf-native-integration; no live GUI E2E in CI
Completion evidence for the ledger: real native-parser-crash/hang-survival-with-metadata-card result; page-anchor survive-reopen result; PG-12/PG-22 evidence once the real WP-13 artifact lands
Notes: Flagged as an early risk proof because AT-05 (PDF first-class attachment) cannot be met by a metadata fallback per PD-07, and the native dependency chain (WP-11.09 -> WP-13) is currently the least-built part of the whole Notes surface - worth surfacing early rather than discovering it late.
```

```text
Execute ArcForges delivery task NOTES.10 — Undo, history, checkpoint and trash as four distinct mechanisms.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-10 (python tools/delivery.py claim NOTES.10 --worker <name>); task branch task/notes-10 in ArcNotes; ledger record ledger/tasks/notes-10.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Session undo (composite grouping, selection-restoring, coalescing boundaries, agent-edit attribution, remote-change rebase-never-retarget), document history, explicit checkpoints and trash-with-restore exist as four independently behaving mechanisms, none substituting for another.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-18.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.05
- WP-18.00 (P2-010 closure: disabled stale undo with original recoverable inverse, no unspecified rebase (undo portion)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.00
- WP-18:p2-010-required-behavior-and-closure-bot P2-010 required behavior and closure (bottom of file): stable run/atom/cell IDs, NotesTextPosition/NotesCommand, explicit IME conflict preservation, disabled stale undo with original recoverable inverse, no unspecified rebase (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, package-level obligation

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.02: EditTransaction computed inverses
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Application/Undo/**; ArcNotes:src/ArcForges.ArcNotes.Application/History/**; ArcNotes:tests/ArcForges.ArcNotes.Tests/Application/Undo/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcnotes-migrations (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: NOTES.14, NOTES.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests: distinction matrix, restore-from-trash, checkpoint restore, undo-is-not-crash-recovery test, undo-selection test, coalescing-boundary test, agent-edit undo/attribution test, rebase test
Completion evidence for the ledger: four-mechanism distinction matrix, undo-selection and undo-rebase results per WP-18.05 completion gate
```

```text
Execute ArcForges delivery task NOTES.11 — Crash recovery and upgrade/downgrade migration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-11 (python tools/delivery.py claim NOTES.11 --worker <name>); task branch task/notes-11 in ArcNotes; ledger record ledger/tasks/notes-11.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Kill-during-edit/migration and corrupted-tail recovery reach the last committed boundary with explicit loss reporting; migration from every prior schema version preserves semantics against golden fixtures; downgrade is defined (reverse migration or clean refusal).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-18.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.06

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.02: the journal/recovery pipeline and StorageSchemaVersion migration apparatus
- [artifact] PLT.03: real snapshot and crash/corruption recovery
- [artifact] PLT.04: the real migration runner and StorageSchemaVersion apparatus
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Infrastructure/Migrations/**; ArcNotes:tests/ArcForges.ArcNotes.Tests/Recovery/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcnotes-migrations (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: NOTES.14, NOTES.29

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests: kill-during-edit, kill-during-migration, corrupted-tail recovery, migration-from-every-fixture with semantic comparison, downgrade-refusal test
Completion evidence for the ledger: recovery matrix and migration semantic-comparison results per WP-18.06 completion gate
```

```text
Execute ArcForges delivery task NOTES.12 — ArcNotes capability surface registration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-12 (python tools/delivery.py claim NOTES.12 --worker <name>); task branch task/notes-12 in ArcNotes; ledger record ledger/tasks/notes-12.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: ArcNotes registers query/read/create/edit/artifact-production capabilities each with risk level, side-effect class, reversibility and approval posture; owner-side validation refuses regardless of caller assertion.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-18.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.07

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.18: the Platform capability/resource contribution model (capability/extension descriptor package)
- [contract] CON.91: CapabilityArguments, CapabilityResult, ToolProposal, ToolResult wire records
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.AssistantIntegration/**; ArcNotes:tests/ArcForges.ArcNotes.Tests/AssistantIntegration/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcnotes-composition (append): Each feature registers services and capabilities through its own registration module; the composition root only lists modules; ordering conflicts are resolved at merge.
Unblocks: HAR.05, NOTES.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests: capability descriptor validation, owner-side refusal tests, idempotency test per write capability
Completion evidence for the ledger: capability descriptor and owner-side refusal results per WP-18.07 completion gate
Notes: Sequenced after NOTES.01/02/06/07/08 conceptually (it exposes their operations) but the registry scaffolding itself can start as soon as WP-09 is available; individual descriptor entries land with their owning feature task.
```

```text
Execute ArcForges delivery task NOTES.13 — ArcNotes reference-matrix drift check (AFFiNE/SiYuan).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-13 (python tools/delivery.py claim NOTES.13 --worker <name>); task branch task/notes-13 in ArcNotes; ledger record ledger/tasks/notes-13.md.
Kind/size: governance/S. Baseline: not-started.
Outcome: A drift report compares the bound AFFiNE (81df4751a3) and SiYuan (eef105683) commits against their current upstream state, assesses any newly introduced material against accepted ArcNotes scope, and re-verifies the AFFiNE licence split (packages/backend, packages/common/native remain proprietary).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-18.08 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.08

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:docs/reference-drift/arcnotes-affine-siyuan.md
Unblocks: NOTES.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): documentation/evidence task only; no product build required beyond reading the two reference trees' current state and licence files
Completion evidence for the ledger: drift report listing changed rows, new material with assessment, and licence re-confirmation, per WP-18.08 completion gate
Notes: No code dependency; can run at any time, fully in parallel with every other NOTES task. Explicitly NOT a baseline audit - PG-01 and F-013 were already closed pre-package.
```

```text
Execute ArcForges delivery task NOTES.14 — Owned-artifact and real-integration verification.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-14 (python tools/delivery.py claim NOTES.14 --worker <name>); task branch task/notes-14 in ArcNotes; ledger record ledger/tasks/notes-14.md.
Kind/size: acceptance/M. Baseline: not-started.
Outcome: Independent editor/store/recovery fixtures, helper isolation and content-origin/attachment checks are recorded against the real staged artifacts consumed at this point; the package is not signed off while any contract/owner/recovery rule still needs design during coding.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-18.90 (all work except the parts mapped to NOTES.02): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.90
- WP-18.00 (final-review paragraph: independent verification of 02-desktop-data-model; scalar-definition fixtures follow the fixed profile): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.00
- WP-18:final-review-paragraph-s5-before-18-90-i Final-review paragraph (S5, before 18.90): independent verification of 02-desktop-data-model; typed structural outbox entries; multi-root local tokens; complete move classification mapping/preview; offline create->move->edit and crash-before/after-acknowledgement test; scalar-definition fixtures follow the fixed profile (WP-28 repeats with real property/view UI) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, package-level obligation

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.01: own-lane completion
- [artifact] NOTES.02: own-lane completion
- [artifact] NOTES.03: own-lane completion
- [artifact] NOTES.04: own-lane completion
- [artifact] NOTES.05: own-lane completion
- [artifact] NOTES.06: own-lane completion
- [artifact] NOTES.07: own-lane completion
- [artifact] NOTES.08: own-lane completion
- [artifact] NOTES.09: own-lane completion (fixture-parser scope only; real PDFium is separately tracked)
- [artifact] NOTES.10: own-lane completion
- [artifact] NOTES.11: own-lane completion
- [artifact] NOTES.12: own-lane completion
- [artifact] NOTES.13: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:docs/release-notes.md; ArcNotes:tests/ArcForges.ArcNotes.Tests/Integration/Wp18/**
Unblocks: REL.01

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline initial-state matrix rows applicable to this product (fresh shell, hydrated outage, unavailable content, signout, restart); no macOS/hosted-runtime CI
Completion evidence for the ledger: owned artifact and real-integration receipt: source commit, producer version, candidate hashes, actual runtime/OS/device/provider, scenario, result, limitations, real-vs-fixture status per WP-18.90
```

```text
Execute ArcForges delivery task NOTES.15 — Local full-text index over hydrated content.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-15 (python tools/delivery.py claim NOTES.15 --worker <name>); task branch task/notes-15 in ArcNotes; ledger record ledger/tasks/notes-15.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: An incremental FTS index over document/block content, properties, tags and attachment-extracted text follows the write path, never diverges after a crash, rebuilds fully from canonical data, and meets query latency budget on the scale corpus.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-19.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\19-arcnotes-search-and-portability.md, anchor rule-wp-19.00

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.02: block content to index
- [artifact] PLT.07: journal-driven derived-store update pattern (data-model 03 S1: DS-01..DS-07)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Search/Index/**; ArcNotes:tests/ArcForges.ArcNotes.Tests/Search/Index/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcnotes-composition (append): Each feature registers services and capabilities through its own registration module; the composition root only lists modules; ordering conflicts are resolved at merge.
Unblocks: NOTES.16, NOTES.17, NOTES.22

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests: divergence test after crash mid-index-update, full-rebuild-equivalence test, latency measurement against the scale corpus
Completion evidence for the ledger: index divergence, rebuild-equivalence and latency results per WP-19.00 completion gate
Notes: implementation-sequence.md S3's 'What may be mocked' table explicitly lists 'Local full-text indexing and citation anchors' under 'Must be real early' (Cloud search may be mocked, this may not) - flagged as an early risk proof accordingly.
```

```text
Execute ArcForges delivery task NOTES.16 — Query, ranking and permission over the local index.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-16).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-16 (python tools/delivery.py claim NOTES.16 --worker <name>); task branch task/notes-16 in ArcNotes; ledger record ledger/tasks/notes-16.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Query supports text/property/tag/structural filters with explainable basic ranking; permission is applied during evaluation so a refused document never influences results or counts, including bounded notes.scalar.v1 predicates on the local hydrated path.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-19.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\19-arcnotes-search-and-portability.md, anchor rule-wp-19.01

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.15: the FTS index to query
- [artifact] NOTES.07: property/tag store
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Search/Query/**; ArcNotes:tests/ArcForges.ArcNotes.Tests/Search/Query/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcnotes-composition (append): Each feature registers services and capabilities through its own registration module; the composition root only lists modules; ordering conflicts are resolved at merge.
Unblocks: NOTES.18, NOTES.22, NOTES.24

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests: filter coverage tests, permission test (refused content invisible in results and counts), ranking stability test
Completion evidence for the ledger: filter/permission/ranking results per WP-19.01 completion gate
```

```text
Execute ArcForges delivery task NOTES.17 — Citation anchors.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-17).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-17 (python tools/delivery.py claim NOTES.17 --worker <name>); task branch task/notes-17 in ArcNotes; ledger record ledger/tasks/notes-17.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: search_anchor rows (block_id, offset range, content_fingerprint) survive insert/delete/reorder/reparent edits where the cited content still exists, and report invalidity explicitly rather than drifting.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-19.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\19-arcnotes-search-and-portability.md, anchor rule-wp-19.02

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.15: search index/derived-store plumbing
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Search/Anchors/**; ArcNotes:tests/ArcForges.ArcNotes.Tests/Search/Anchors/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: NOTES.22

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests: anchor survival across insert/delete/reorder/reparent, explicit-invalid test after content removal
Completion evidence for the ledger: anchor survival and invalidity results per WP-19.02 completion gate
Notes: Also covered by the 'must be real early' scaffolding table entry for citation anchors (see NOTES.15).
```

```text
Execute ArcForges delivery task NOTES.18 — Saved views (list projection only).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-18).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-18 (python tools/delivery.py claim NOTES.18 --worker <name>); task branch task/notes-18 in ArcNotes; ledger record ledger/tasks/notes-18.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: A saved_view row (notebook scope, query profile, semantic-definition bindings, view revision) produces a list projection; deleting a view never deletes content; results always reflect current data. Full typed query/table delivery is explicitly NOT emulated here - it is WP-28 (NOTES.24/26).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-19.03 (full - eq/ne/isMissing/isPresent for all declared scalar kinds, all/any/not composition, DocumentId ordering under the profile bounds; later value operators and property sorting explicitly unavailable until WP-28): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\19-arcnotes-search-and-portability.md, anchor rule-wp-19.03
- WP-19:s8-additional-completion-requirement-the S8 additional completion requirement: the initial view stores the final profile/bindings; neither invents a temporary semantic profile nor claims full table/query delivery before WP-28 (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\19-arcnotes-search-and-portability.md, package-level obligation

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.16: query evaluation
- [artifact] NOTES.07: property definitions
- [contract] CON.91: SavedViewRecord, NotesQuery, NotesFilter, ScalarPredicate wire records
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Search/SavedViews/**; ArcNotes:tests/ArcForges.ArcNotes.Tests/Search/SavedViews/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcnotes-composition (append): Each feature registers services and capabilities through its own registration module; the composition root only lists modules; ordering conflicts are resolved at merge.; RES-arcnotes-migrations (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: NOTES.22, NOTES.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests: ownership test (deletion non-destructive), re-evaluation test (results reflect current content)
Completion evidence for the ledger: saved-view ownership and freshness results per WP-19.03 completion gate
```

```text
Execute ArcForges delivery task NOTES.19 — Non-destructive Markdown/plain-text import (incl. Obsidian-style folders).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-19).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-19 (python tools/delivery.py claim NOTES.19 --worker <name>); task branch task/notes-19 in ArcNotes; ledger record ledger/tasks/notes-19.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Import from Markdown/plain-text sources (including an Obsidian-style vault layout) produces a reviewable import plan then a report of created/transformed/skipped items; the source is never modified; a partial failure leaves a coherent result and clear report.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-19.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\19-arcnotes-search-and-portability.md, anchor rule-wp-19.04

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.01: notebook/document placement
- [artifact] NOTES.02: EditTransaction write path (origin=import)
- [artifact] NOTES.06: link resolution
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.ImportExport/Import/**; ArcNotes:fixtures/formats/import/**; ArcNotes:tests/ArcForges.ArcNotes.Tests.Integration/Import/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcnotes-composition (append): Each feature registers services and capabilities through its own registration module; the composition root only lists modules; ordering conflicts are resolved at merge.; RES-arcnotes-format-fixtures (append): Fixtures are added per task under its own subdirectory; manifests are append-only; golden fixtures are never regenerated to pass a test.
Unblocks: NOTES.22

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit/integration tests: import from every declared source fixture, source-immutability assertion, induced-failure test asserting coherent partial result with report
Completion evidence for the ledger: per-source import results, immutability assertion, partial-failure report per WP-19.04 completion gate; this is ArcNotes' PG-07 contribution (import fixture obligation, not export)
Notes: No native/ContentSandbox dependency - Markdown/plain-text parsing is managed-code text parsing, unlike PDF/image attachments.
```

```text
Execute ArcForges delivery task NOTES.20 — Cloud Notes export client and its named fixture endpoint.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-20).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-20 (python tools/delivery.py claim NOTES.20 --worker <name>); task branch task/notes-20 in ArcNotes; ledger record ledger/tasks/notes-20.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: The Notes Cloud-export client builds a snapshot request over acknowledged revisions and validates the returned Markdown/attachments/metadata/fidelity-report shape against a named, registered fixture endpoint; the client itself is real and complete, only the server side is a fixture.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-19.05 (full - client-side export flow, fidelity manifest, offline-refuses-new-export-without-losing-drafts behaviour): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\19-arcnotes-search-and-portability.md, anchor rule-wp-19.05
- WP-19:s6-impacts-no-notes-printing-pdf-export S6 Impacts: no Notes printing/PDF-export feature is added (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\19-arcnotes-search-and-portability.md, package-level obligation

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.01: acknowledged-revision snapshot source
- [contract] CON.91: ArtifactRef and ExportRequest-shaped wire records (INotesOperations.ExportAsync returns ArtifactRef per architecture/contracts/02-local-rpc-operations.md)
- [contract] CON.20: published notes.requestExport and export records
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.45: the real Cloud Notes export producer (bounded leased export job, acknowledged-revision manifest, verified expiring download artifact)

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.ImportExport/Export/**; ArcNotes:tests/ArcForges.ArcNotes.Tests.Integration/Export/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcnotes-composition (append): Each feature registers services and capabilities through its own registration module; the composition root only lists modules; ordering conflicts are resolved at merge.
Permitted substitutes (never real integration evidence): SUB-notes-cloud-export: client-side export request construction, fidelity-report rendering, attachment-hash verification, offline-refusal behaviour against a scripted endpoint Real producer ['CLOUD.45']; removed by NOTES.33
Unblocks: NOTES.22, NOTES.30, NOTES.33

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit/integration tests against the named fixture: acknowledged-source snapshot identity, attachment hashes, metadata/link fidelity, complete loss entries; Cloud-unavailable-refuses-new-export test; no live Cloud call in this task's own CI
Completion evidence for the ledger: Cloud export content, attachment-hash, link-manifest and fidelity results (against the fixture) per WP-19.05 completion gate; real producer evidence recorded separately at WP-25.08/IM.notes-cloud-export
Notes: This task must register its fixture endpoint in a way IM.notes-cloud-export can structurally assert was removed (implementation-sequence.md TS-01/TS-02: 'scaffolding is deleted, never adapted'; the deleting package is WP-25.08, owned by the Cloud lane, so ArcNotes' obligation is to make the fixture registration a single removable seam).
```

```text
Execute ArcForges delivery task NOTES.21 — Repository-projection prohibition (structural assertion).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-21).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-21 (python tools/delivery.py claim NOTES.21 --worker <name>); task branch task/notes-21 in ArcNotes; ledger record ledger/tasks/notes-21.md.
Kind/size: governance/S. Baseline: not-started.
Outcome: A dependency-policy test fails the build on any Git or LFS client package reference from any ArcNotes project; a structural test asserts no type implements or is named as a projection writer; the exclusion is explained in the product UI rather than merely absent.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-19.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\19-arcnotes-search-and-portability.md, anchor rule-wp-19.06

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.03: the dependency-policy analyzer infrastructure
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:eng/policy/dependency-policy.json; ArcNotes:tests/ArcForges.ArcNotes.Tests/DependencyPolicyTests.cs
Unblocks: NOTES.22

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline static/dependency-policy test only
Completion evidence for the ledger: dependency-policy, structural and presentation results proving no repository-projection or Git/LFS path exists, per WP-19.06 completion gate
Notes: Can run essentially any time in parallel; minimal real dependency since the governance tooling it extends already exists in the repo.
```

```text
Execute ArcForges delivery task NOTES.22 — Owned-artifact and real-integration verification.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-22).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-22 (python tools/delivery.py claim NOTES.22 --worker <name>); task branch task/notes-22 in ArcNotes; ledger record ledger/tasks/notes-22.md.
Kind/size: acceptance/M. Baseline: not-started.
Outcome: Independent import/search/export and missing-resource outcomes are recorded; public value profiles and owner authorization remain compatible; no Git mirror, DOCX or newly invented export suite exists.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-19.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\19-arcnotes-search-and-portability.md, anchor rule-wp-19.90

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.15: own-lane completion
- [artifact] NOTES.16: own-lane completion
- [artifact] NOTES.17: own-lane completion
- [artifact] NOTES.18: own-lane completion
- [artifact] NOTES.19: own-lane completion
- [artifact] NOTES.20: own-lane completion (fixture scope)
- [artifact] NOTES.21: own-lane completion
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:tests/ArcForges.ArcNotes.Tests/Integration/Wp19/**
Unblocks: REL.01

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline initial-state matrix rows applicable to this product; no macOS/hosted-runtime CI
Completion evidence for the ledger: owned artifact and real-integration receipt per WP-19.90
```

```text
Execute ArcForges delivery task NOTES.23 — Typed property schemas: full bounded scalar set.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-23).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-23 (python tools/delivery.py claim NOTES.23 --worker <name>); task branch task/notes-23 in ArcNotes; ledger record ledger/tasks/notes-23.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Property definitions cover text, number, date, dateTime, single-select, multi-select, checkbox, URL with exact notes.scalar.v1 encodings; relation and derived are structurally excluded (no join engine, no formula evaluator); a full lifecycle (create/rename/type-change-with-preview/delete) is enforced with no silent data loss.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-28.00 (full - all eight declared scalar kinds/config bounds/exact encodings; rename preserves semantic bindings; dependent type/option changes refused after preview; trashed definitions make views visibly invalid): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, anchor rule-wp-28.00
- WP-28:final-review-paragraph-s5-before-28-90-i Final-review paragraph (S5, before 28.90): independent verification of 04-protobuf-wire-registry; cross-notebook move with real scalar definitions/select options/tags - stale target semantics, incomplete mapping and conflicting destination mappings refuse atomically; explicit approved removals remain in history (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, package-level obligation

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.07: the basic document-level property model this extends
- [contract] CON.91: PropertyDefinition.type/profile/numberScale/semanticRevision fields and the notesQuery/scalarPredicate/scalarValue constraint rules
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Database/Properties/**; ArcNotes:fixtures/formats/arcnotes/**; ArcNotes:tests/ArcForges.ArcNotes.Tests.Integration/Properties/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcnotes-format-fixtures (append): Fixtures are added per task under its own subdirectory; manifests are append-only; golden fixtures are never regenerated to pass a test.; RES-arcnotes-migrations (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: NOTES.24, NOTES.28, NOTES.29, NOTES.30, NOTES.32

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit/integration tests: type validation per kind, rename-preserves-values test, type-change-stated-behaviour test, deletion-stated-consequence test
Completion evidence for the ledger: property lifecycle results with no silent loss per WP-28.00 completion gate
```

```text
Execute ArcForges delivery task NOTES.24 — Query model: local evaluator and notes.scalar.v1 conformance fixtures.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-24).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-24 (python tools/delivery.py claim NOTES.24 --worker <name>); task branch task/notes-24 in ArcNotes; ledger record ledger/tasks/notes-24.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: A local query evaluator over properties/tags/links/content/structure implements notes.scalar.v1 exactly (operators, missing/isMissing/isPresent semantics, AST bounds, stable sort with DocumentId tiebreak, dataset-token pagination) with permission applied during evaluation and stability under concurrent mutation, proven against a committed fixture-vector suite usable by both native and Cloud evaluators.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-28.01 (local evaluator + fixture-based conformance suite covering every v1 operator, boolean/missing behaviour, AST limit, ordinal/decimal/instant comparison, signed dataset-bound pagination): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, anchor rule-wp-28.01
- WP-28:s8-additional-completion-requirement-eve S8 additional completion requirement: every scalar/query/profile vector passes on both owners; all supported list/table operations implemented without new product design choices (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, package-level obligation

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.23: full property schema
- [artifact] NOTES.16: the existing local query/permission plumbing from WP-19.01
- [contract] CON.91: the complete notes.scalar.v1 wire vocabulary (ScalarPredicate, ScalarValue, NotesQuery, NotesFilter, FilterGroup, NotesSort, PageRequest) and its constraints.json AST-bound rules
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] NOTES.34: cross-evaluator conformance against the real Cloud (D1-backed) evaluator

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Database/Query/**; ArcNotes:tests/ArcForges.ArcNotes.Tests.Integration/Query/**
Shared resources (follow the owner protocol): RES-notes-scalar-vectors (append): Vectors are published by Contracts; the ArcNotes and Cloud evaluators consume the same published vectors; changes are contract changes.
Unblocks: NOTES.26, NOTES.32, NOTES.34

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit/integration tests: predicate coverage, permission test, stability-under-concurrent-mutation test; the fixture vectors from arcnotes.md S7.1 acceptance-vectors paragraph (D1 to D4 ordering, ne semantics, numeric/checkbox/offset equality) run without any live Cloud dependency
Completion evidence for the ledger: query permission and stability results per WP-28.01 completion gate (local portion); cross-evaluator match is IM.notes-cloud-query-conformance's evidence
Notes: This is the clearest example in this area of the 'aggregate producer gate' pattern to avoid: WP-28.01's text bundles the local evaluator and the Cloud cross-check into one substep, but only the cross-check genuinely needs a real Cloud artifact. Modelled as one local task (NOTES.24) plus a separate integration proposal (IM.notes-cloud-query-conformance) rather than making the whole substep wait.
```

```text
Execute ArcForges delivery task NOTES.26 — View kinds: list and table projections.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-26).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-26 (python tools/delivery.py claim NOTES.26 --worker <name>); task branch task/notes-26 in ArcNotes; ledger record ledger/tasks/notes-26.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Table and list views project the same NOTES.24 query with identical ordering (missing last, ascending DocumentId tiebreak); switching kinds preserves the query; deleting a view destroys no content. Board/gallery/calendar/timeline are structurally absent, not merely unimplemented.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-28.02 (full - list/table projections with visible-properties/sorting/filtering configuration, D1 to D4/numeric/checkbox/offset/equal-key/mutation-restart vectors, kind-switch preserves query): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, anchor rule-wp-28.02
- WP-28:s8-additional-completion-requirement-eve S8 additional completion requirement: every scalar/query/profile vector passes on both owners; all supported list/table operations implemented without new product design choices (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, package-level obligation

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.24: the query evaluator
- [artifact] NOTES.18: the WP-19.03 saved-view list projection this extends to table+full filter/sort depth
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Database/Views/**; ArcNotes:src/ArcForges.ArcNotes.Presentation/Views/**; ArcNotes:tests/ArcForges.ArcNotes.Tests.Integration/Views/**
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcnotes-composition (append): Each feature registers services and capabilities through its own registration module; the composition root only lists modules; ordering conflicts are resolved at merge.
Unblocks: NOTES.27, NOTES.29, NOTES.30, NOTES.31, NOTES.32

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit/integration tests: per-kind rendering/interaction tests, kind-switch-preserves-query test, ownership test
Completion evidence for the ledger: per-kind projection, switch and ownership results per WP-28.02 completion gate
```

```text
Execute ArcForges delivery task NOTES.27 — Editing through a view.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-27).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-27 (python tools/delivery.py claim NOTES.27 --worker <name>); task branch task/notes-27 in ArcNotes; ledger record ledger/tasks/notes-27.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Property values are editable directly in a view, going through the same EditTransaction write path (SetProperty) as document editing, with full validation and permission - never a shortcut.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-28.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, anchor rule-wp-28.03

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.26: the view surface to edit through
- [artifact] NOTES.02: the single EditTransaction write path (SetProperty operation)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Presentation/Views/Editing/**; ArcNotes:tests/ArcForges.ArcNotes.Tests.Integration/Views/Editing/**
Unblocks: NOTES.32

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests: write-path assertion, validation test, permission test
Completion evidence for the ledger: view-edit write-path, validation and permission results per WP-28.03 completion gate
```

```text
Execute ArcForges delivery task NOTES.28 — Lightness preservation for plain notes.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-28).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-28 (python tools/delivery.py claim NOTES.28 --worker <name>); task branch task/notes-28 in ArcNotes; ledger record ledger/tasks/notes-28.md.
Kind/size: governance/S. Baseline: not-started.
Outcome: A plain note with no properties carries no property panel, no schema, no measurable performance cost; the property system is opt-in per document and per collection.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-28.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, anchor rule-wp-28.04

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.23: the property schema whose absence is being proven cost-free
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:tests/ArcForges.ArcNotes.Tests.Integration/Lightness/**
Unblocks: NOTES.32

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit test: default-experience assertion (new note requires nothing) plus a performance comparison asserting no regression for property-free documents
Completion evidence for the ledger: lightness default and performance comparison per WP-28.04 completion gate
```

```text
Execute ArcForges delivery task NOTES.29 — Supported-schema migration for property/view data (local).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-29).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-29 (python tools/delivery.py claim NOTES.29 --worker <name>); task branch task/notes-29 in ArcNotes; ledger record ledger/tasks/notes-29.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Every actually-shipped scalar-property/list/table schema version upgrades preserving stable IDs and additive unknown fields, with no canvas-era or invented historical fixture.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-28.05 (supported-schema migration: actual shipped scalar-property/list/table schemas migrate preserving stable IDs and additive fields; reading additive unknown fields): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, anchor rule-wp-28.05

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.11: the migration framework this extends to property/view tables
- [artifact] NOTES.23: the schemas being migrated
- [artifact] NOTES.26: the view schemas being migrated
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Infrastructure/Migrations/**; ArcNotes:fixtures/formats/arcnotes/**
Shared resources (follow the owner protocol): RES-arcnotes-format-fixtures (append): Fixtures are added per task under its own subdirectory; manifests are append-only; golden fixtures are never regenerated to pass a test.; RES-arcnotes-migrations (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: NOTES.32

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests: upgrade every historical supported schema, read additive unknown fields
Completion evidence for the ledger: supported-schema migration result (local portion) per WP-28.05 completion gate
Notes: Split from the export-fidelity half of WP-28.05 (NOTES.30) because migration needs no Cloud artifact at all, while export fidelity explicitly needs the real WP-25.08 producer - keeping them together would make a purely-local schema-migration task wait on Cloud for no reason.
```

```text
Execute ArcForges delivery task NOTES.30 — Cloud export fidelity for property/view metadata.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-30).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-30 (python tools/delivery.py claim NOTES.30 --worker <name>); task branch task/notes-30 in ArcNotes; ledger record ledger/tasks/notes-30.md.
Kind/size: feature/S. Baseline: not-started.
Outcome: The Cloud export manifest built by NOTES.20 additionally declares property/view metadata with an accurate fidelity report, verified against the real WP-25.08 export producer (not a mock).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-28.05 (Cloud export includes declared property/view metadata and a fidelity report, verified through the real WP-25.08 producer): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, anchor rule-wp-28.05
- WP-28:p2-010-required-behavior-and-closure-bot P2-010 required behavior and closure (bottom of file): verify local hydrated/pending export + actual Cloud export; source-policy/one-use context permission; notebook/document/query/structural conflict behavior (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, package-level obligation

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.20: the Cloud export client this extends
- [artifact] NOTES.23: property schema to describe in the manifest
- [artifact] NOTES.26: view schema to describe in the manifest
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] NOTES.33: real Cloud export producer, same as NOTES.20

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.ImportExport/Export/PropertyViewFidelity/**
Shared resources (follow the owner protocol): RES-arcnotes-composition (append): Each feature registers services and capabilities through its own registration module; the composition root only lists modules; ordering conflicts are resolved at merge.
Unblocks: NOTES.33

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): integration test against the real WP-25.08 producer once available; no mock Cloud acceptance permitted per producer-artifacts-and-integration.md row 28
Completion evidence for the ledger: supported-schema migration and Cloud-export fidelity results (export portion) per WP-28.05 completion gate
```

```text
Execute ArcForges delivery task NOTES.31 — Scale: large collections, many properties, large result sets.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-31).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-31 (python tools/delivery.py claim NOTES.31 --worker <name>); task branch task/notes-31 in ArcNotes; ledger record ledger/tasks/notes-31.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Every view kind meets responsiveness and memory budgets on the scale corpus through virtualisation and indexing; a soak test on a large view holds memory within the product ceiling.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-28.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, anchor rule-wp-28.06

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.26: the view kinds being scale-tested
- [artifact] NOTES.04: the virtualised layout engine reused for large table/list bodies
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:tests/ArcForges.ArcNotes.Tests.Integration/Scale/**
Unblocks: NOTES.32

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline scale-corpus benchmark fixtures; memory-ceiling assertion; soak test
Completion evidence for the ledger: scale corpus and soak results per view kind, per WP-28.06 completion gate
```

```text
Execute ArcForges delivery task NOTES.32 — Owned-artifact and real-integration verification.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-32).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/notes-32 (python tools/delivery.py claim NOTES.32 --worker <name>); task branch task/notes-32 in ArcNotes; ledger record ledger/tasks/notes-32.md.
Kind/size: acceptance/M. Baseline: not-started.
Outcome: Independent local/Cloud query vectors, null/missing/invalid values, sorting/tie-breaks and snapshot pagination are recorded; the producer edge to WP-40 is kept (WP-28 provides for WP-40, never blocks on it).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-28.90 (all work except the parts mapped to NOTES.34): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, anchor rule-wp-28.90
- WP-28.00 (final-review paragraph: independent verification of 04-protobuf-wire-registry; cross-notebook move with real scalar defs/select options/tags): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, anchor rule-wp-28.00
- WP-28:final-review-paragraph-s5-before-28-90-i Final-review paragraph (S5, before 28.90): independent verification of 04-protobuf-wire-registry; cross-notebook move with real scalar definitions/select options/tags - stale target semantics, incomplete mapping and conflicting destination mappings refuse atomically; explicit approved removals remain in history (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, package-level obligation
- WP-28:p2-010-required-behavior-and-closure-bot P2-010 required behavior and closure (bottom of file): verify local hydrated/pending export + actual Cloud export; source-policy/one-use context permission; notebook/document/query/structural conflict behavior (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, package-level obligation

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.23: own-lane completion
- [artifact] NOTES.24: own-lane completion
- [artifact] NOTES.26: own-lane completion
- [artifact] NOTES.27: own-lane completion
- [artifact] NOTES.28: own-lane completion
- [artifact] NOTES.29: own-lane completion
- [artifact] NOTES.31: own-lane completion
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] NOTES.34: the real local-vs-Cloud query conformance evidence WP-28.90 explicitly requires
- [integration] NOTES.33: NOTES.30's real producer evidence

Permitted write scope: ArcNotes:tests/ArcForges.ArcNotes.Tests/Integration/Wp28/**
Unblocks: REL.01

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline where possible; real Cloud cross-check evidence attached from IM.notes-cloud-query-conformance; no macOS/hosted-runtime CI
Completion evidence for the ledger: owned artifact and real-integration receipt per WP-28.90, including local/Cloud query vector parity and export fidelity
```

```text
Execute ArcForges delivery task NOTES.33 — Real Cloud Notes export join replaces the / fixture endpoint.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-33).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes). Also touches: Cloud.
Claim and handoff record: claims/notes-33 (python tools/delivery.py claim NOTES.33 --worker <name>); task branch task/notes-33 in ArcNotes; ledger record ledger/tasks/notes-33.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Real host/database/object-store Notes export across concurrent edits, notebook moves, deleted attachments, quota limits, expiry, restart, cancellation and paid-term end; structural removal of the runtime fixture registration NOTES.20 created

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-28.05 (Cloud export fidelity for property/view metadata): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, anchor rule-wp-28.05
- WP-25.08 (Notes/Chat export producer (owned by the Cloud lane; Chat half is the assistant lanes WP-15.06)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.08

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.20: real, delivered outcome of NOTES.20 (Cloud Notes export client and its named fixture endpoint)
- [artifact] NOTES.30: real, delivered outcome of NOTES.30 (Cloud export fidelity for property/view metadata)
- [artifact] CLOUD.45: real, delivered outcome of CLOUD.45 (Real Cloud Notes and Chat export producers)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: CLOUD.47, CLOUD.58, NOTES.30, NOTES.32

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: Real host/database/object-store Notes export across concurrent edits, notebook moves, deleted attachments, quota limits, expiry, restart, cancellation and paid-term end; structural removal of the runtime fixture registration NOTES.20 created
```

```text
Execute ArcForges delivery task NOTES.34 — Cross-evaluator conformance of notes.scalar.v1 between the native cache and the real Cloud query evaluator.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-34).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes). Also touches: Cloud.
Claim and handoff record: claims/notes-34 (python tools/delivery.py claim NOTES.34 --worker <name>); task branch task/notes-34 in ArcNotes; ledger record ledger/tasks/notes-34.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Identical operator, ordering and pagination semantics between ArcNotes' local evaluator (NOTES.24) and Cloud's D1-backed evaluator, on the same authorized, fully hydrated revision set, per the arcnotes.md S7.1 acceptance vectors

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-28.01 (native-vs-Cloud conformance suite execution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, anchor rule-wp-28.01
- WP-28.90 (independent local/Cloud query vectors, no mock Cloud acceptance): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\28-arcnotes-properties-and-views.md, anchor rule-wp-28.90

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.24: real, delivered outcome of NOTES.24 (Query model: local evaluator and notes.scalar.v1 conformance fixtures)
- [artifact] CLOUD.37: real, delivered outcome of CLOUD.37 (Cloud Notes authority and sync scopes)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: NOTES.24, NOTES.32

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: Identical operator, ordering and pagination semantics between ArcNotes' local evaluator (NOTES.24) and Cloud's D1-backed evaluator, on the same authorized, fully hydrated revision set, per the arcnotes.md S7.1 acceptance vectors
```

```text
Execute ArcForges delivery task NOTES.35 — ArcNotes participates in the three-device convergence harness.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-35).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes). Also touches: Cloud.
Claim and handoff record: claims/notes-35 (python tools/delivery.py claim NOTES.35 --worker <name>); task branch task/notes-35 in ArcNotes; ledger record ledger/tasks/notes-35.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: ArcNotes documents/blocks/attachments/deletions converge to verifiably identical state across three devices under concurrent editing, an extended offline device, and a mid-sync crash

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.07 (Notes object-kind coverage of the convergence harness; the real ArcNotes-client side of the three-device convergence harness): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.07

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NOTES.01: real, delivered outcome of NOTES.01 (Notebook/folder hierarchy, document placement and structural commands)
- [artifact] NOTES.02: real, delivered outcome of NOTES.02 (Block/inline content model, EditTransaction engine, kind conversions and clipboard)
- [artifact] NOTES.10: real, delivered outcome of NOTES.10 (Undo, history, checkpoint and trash as four distinct mechanisms)
- [artifact] CLOUD.44: real, delivered outcome of CLOUD.44 (Multi-device convergence harness)
- [artifact] CLOUD.37: real, delivered outcome of CLOUD.37 (Cloud Notes authority and sync scopes)
- [artifact] CLOUD.38: real, delivered outcome of CLOUD.38 (Client outbox and conflict lineage (desktop data model))
- [artifact] CLOUD.39: real, delivered outcome of CLOUD.39 (Guarded publication and convergent bootstrap)
- [artifact] CLOUD.40: real, delivered outcome of CLOUD.40 (Conflict detection and five resolution policies)
- [artifact] CLOUD.41: real, delivered outcome of CLOUD.41 (Deletion and tombstones)
- [artifact] CLOUD.42: real, delivered outcome of CLOUD.42 (Blob lifecycle (real R2 staged/verified/committed))
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: CLOUD.47, NOTES.02

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: ArcNotes documents/blocks/attachments/deletions converge to verifiably identical state across three devices under concurrent editing, an extended offline device, and a mid-sync crash
Notes: Merged duplicate integration or closure task formerly proposed as CLOUD.56.
```

```text
Execute ArcForges delivery task NOTES.37 — ArcNotes PDF attachment viewer against the real ContentSandbox.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcnotes.md (anchor task-notes-37).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes). Also touches: DesktopPlatform.
Claim and handoff record: claims/notes-37 (python tools/delivery.py claim NOTES.37 --worker <name>); task branch task/notes-37 in ArcNotes; ledger record ledger/tasks/notes-37.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: the full PG-12 gate: a malformed/hostile PDF opened through ArcNotes' attachment viewer cannot crash or compromise the parent product, and licence/provenance evidence for the PDF dependency closure is complete.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-18.04 (full - owned by the ArcNotes lane, listed here only because it is the gate-closing consumer of this area's PLT.45; real PDF viewer integration and malformed native input containment): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\18-arcnotes-document-core.md, anchor rule-wp-18.04

Entry condition: adoption slice ADOPT.04.arcnotes is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.45: real, delivered outcome of PLT.45 (Content helper and OS-enforced isolation (ContentSandbox host))
- [artifact] NAT.14: real, delivered outcome of NAT.14 (Pdf family: PDFium and production parser containment in the WP11 helper (NEW library))
- [artifact] NOTES.09: real, delivered outcome of NOTES.09 (PDF in-product viewer, page anchors and native parser isolation)
- [artifact] NAT.25: real, delivered outcome of NAT.25 (Pdf package production: all 6 RIDs + ContentSandbox Runtime.<rid> composition)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: CLOUD.44

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: the full PG-12 gate: a malformed/hostile PDF opened through ArcNotes' attachment viewer cannot crash or compromise the parent product, and licence/provenance evidence for the PDF dependency closure is complete.
Notes: Merged duplicate integration or closure task formerly proposed as NOTES.36.
```
