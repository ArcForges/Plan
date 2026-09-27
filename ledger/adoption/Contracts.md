# Contracts repository adoption

Frozen source: `b10b2f6f316bf0c007e00632c5442fc102ebbe6e`. [Frozen baseline](baseline.md#contracts) retains all exact package coordinates, reviewed instruction PR44, main CI/security and original NuGet/npm/Maven receipts. No open PR existed at freeze. Adoption reviews source only against frozen inputs; later implementation remains separate.

## Retained workflows and package/source ownership

- `.github/workflows/ci.yml`: Linux Build candidate (locked restore, admission/naming/provenance/access, formatting, deterministic generation, compilation, targeted offline tests including serialization AOT, pack), Verify, and source-free original-candidate NuGet/npm/Maven publication. `.github/workflows/security.yml`: dependency review, redacted secret scan, CodeQL C#/JavaScript/Python and Java/Kotlin. No macOS/hosted live/device/browser/GUI/installed-consumer workflow is retained. Existing applicable CI also applies to documentation PRs.
- Package inventory `eng/contract-packages.json`: 14 NuGet, five npm, three Maven identities exactly enumerated in the baseline. Immutable latest frozen NuGet/npm pin `1.0.0-ci.113.1`; Maven original receipt binds `1.0.0-SNAPSHOT` to that exact source/candidate. Notes/Slate LocalRpc source packages are retired pending CON.23; immutable historical publications remain untouched.
- Actual source: public/internal authored proto, `public/http/v1`, `internal/ai-http/v1`, monolithic public/internal constraints; `src/public/dotnet`, `src/internal/dotnet`, public/internal TypeScript owners and `src/public/kotlin`. Existing solution `ArcForges.Contracts.slnx`; no sibling-source dependencies. Generated outputs remain generator-owned, never hand-edited.
- Exact dependency/tool pins remain in `global.json` (SDK 10.0.400, rollForward disabled), Directory.Packages.props and project locks, root npm manifest/lock, Gradle wrapper/version catalogue/strict locks and verification metadata. Adoption changes no pin. Consumers upgrade exact published candidates through their own reviewed change.
- Shared roots: schema source append protocol; generated baseline regenerated after rebase; single Contracts integration owner serializes merge/publication. No adoption edit acquires a product build or deployment lease.

## Combined classifications

Each linked slice contains evidence, actual bindings and remaining scope for its complete lane. No classification here broadens that evidence.

| Task | Classification | Slice |
|---|---|---|
| CON.01 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.02 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.03 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.04 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.05 | inherited with adjustment | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.06 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.07 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.08 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.09 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.10 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.11 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.12 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.13 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.14 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.15 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.16 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.17 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.18 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.19 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.21 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.22 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.23 | inherited with adjustment | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.24 | gap | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.90 | inherited | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.91 | inherited | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| CON.92 | inherited | [adopt-03-contracts](../tasks/adopt-03-contracts.md) |
| EXT.02 | inherited with adjustment | [adopt-03-extensions](../tasks/adopt-03-extensions.md) |
| EXT.04 | gap | [adopt-03-extensions](../tasks/adopt-03-extensions.md) |
| EXT.08 | inherited with adjustment | [adopt-03-extensions](../tasks/adopt-03-extensions.md) |
| GOV.05 | inherited with adjustment | [adopt-03-governance](../tasks/adopt-03-governance.md) |
| GOV.16 | gap | [adopt-03-governance](../tasks/adopt-03-governance.md) |
| REL.07 | gap | [adopt-03-release](../tasks/adopt-03-release.md) |

Only CON.90/91/92 are inherited historical acceptance. Every other task stays open with its listed prerequisites and remaining scope. ADP-10 source retirement is owned by CON.23, with GOV.18 needed for completion; no unresolved new architecture conflict was found. The existing StructuredValue boundary records are reused by EXT.02, not duplicated as a new wire authority.

Validation reused source/receipt/metadata review and ledger consistency, without new builds, public downloads or runtime cycles. Product, provider, device, formal stable release and commercial coverage are not inferred. Each slice's exact reviewed/merge head is in its durable claim/PR; repository record closes only after all four slices are complete in merged Plan.
