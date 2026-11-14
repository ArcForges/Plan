# Codex handoff â€” ArcForges V2

Continue from current GitHub main and the ledger. The owner authorized the original 39 AFV2 tasks and subsequently added all-dependency upgrades with local/CI parity, explicitly requiring document review and merge first. Public activation still needs its separate concrete approval.

## Current authority and document order

Design #66 merged as `7952aa9fbf54613e8c1b078ead797b6f0444f7a7`; Plan #98 merged as `27fe4278d3b30b418619c4369860ddb573caace4` and start-record #99 as `f5fdaabd10a63a5b60d1dce903475b1be2d51b1a`. They established AD-0022/schema3 and the original implementation authorization. Do not redo that completed migration.

The `design/latest-version-policy` / `plan/latest-version-policy` amendment adds AD-0023, R-DEP-001 and AFV2-ENV-01. Inspect its actual PR heads and merged state. Finish independent review and exact-head native Windows/Linux verification; merge Design first, then verify Plan against actual new Design main and merge it. Only after both policy documents merge may actual upgrades begin. Select and install concrete versions during implementation.

## Authorized next work

The graph now has 40 tasks. The original 39-ID authorization remains in the ledger; the added ENV authorization is recorded separately. Read AGENTS, execution-policy, delivery-procedure, acceptance-register and each complete task record. Use `python tools/plan.py next`; start AFV2-ENV-01 after document merge, then resume eligible tasks serially. BASE-01 and MXC-01 both depend on the upgrade. Keep isolated task worktrees, independent nonauthor review and every required native profile; never bypass statuses, hooks, protections or failed safety checks.

ENV covers ArcForges, Cloud, Web, Contracts, shared DesktopPlatform, ArcForges-Design and Plan: all current tools/runtimes/SDKs, Actions/images, direct business dependencies and resolved transitive dependencies. Check latest upstream stable versions during implementation, pin exact identities and make local/CI resolution match. Include major upgrades and necessary compatibility repairs. Preserve immutable historical artifacts, published versions and applied SQL. Independent Mobile/AI/ArcScope/ArcSlate/ArcNotes are protected consumers, outside blanket upgrade scope. Public deployment/activation is not part of ENV.

## Preserved BASE-01 checkpoint

BASE-01 is parked planned, not delivered. Preserve these uncommitted files on Windows under `C:/MyFile/Projects/ArcForges/`:

- `ArcForges/.worktree/afv2-base-01/eng/v2-migration/preflight.py` and `test_preflight.py`; base `10f692224f94916cfc93fbad971f80ec340c5edf`.
- `Cloud/.worktree/afv2-base-01/eng/v2-migration/preflight.py`; base `6df33c525fcbc20495e46c9c4c011086146da796`.
- `Contracts/.worktree/afv2-base-01` remains unmodified at `de3dba76266e89654be9b4d29d097d525a281c6a`.

The earlier Node author diagnostic had 11 tests OK with one Windows condition skipped; the latest protected-fd/in-memory SQLite snapshot and failure-classification changes are untested. Cloud is an untested draft. Consumer scanning, module map, documentation and PostgreSQL fixtures remain unfinished. No product commit, PR or native acceptance exists for this checkpoint. After ENV, reconcile these worktrees with actual upgraded main and run affected checks; do not count the old author diagnostic as current acceptance.

## Product and acceptance boundaries

Deliver the general CLI Sandbox/Run platform with official stable MXC, genuine terminals, preserved intelligent resource management, private persistent data, free offline local CLI, optional free self-hosted Go Center and Blazor management. Only official hosted access is subscription-gated. No product MCP/AI/Task DAG/cache platform/desktop or mobile client; never copy/fork MXC or silently use an uncontained process.

Both composed native profiles need real P1 qualification before executor replacement. Changed upstream versions require relevant source/artifact requalification; dated research is not a new runtime pass. Preserve Node schema15 and Center schema10/11 safeguards and unresolved effects. H-03 blocks destructive admission, not read-only preflight code. Prices/provider/legal/domain settings remain owner inputs, and AFV2-PROD-01 needs separate explicit outward-facing activation approval.

Use the Windows MCP at `C:/MyFile/Projects/ArcForges/` and H-22 Linux MCP at `/home/sammiller/arcforges/`. Fetch independently from GitHub; never substitute WSL/SSH/scratch or transfer verification receipts. Preserve existing dirty primary checkouts. Record exact heads, worktrees and unfinished steps on interruption. Report in Simplified Chinese and continue only within the authorized graph.
