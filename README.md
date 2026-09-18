# ArcForges implementation plan

This local repository provides a linear, single-substep entry into the accepted ArcForges Design. It contains execution navigation and receipts, not a replacement specification.

## Use

1. Open [list.md](list.md). Begin at **00.00 — Product and naming freeze**.
2. Copy that entry's complete code block into the AI task. It points to [the reusable prompt](C:/MyFile/Projects/arcforges-implementation-prompt.md), the exact formal WP section and its reading context. There are no invocation fields to fill out and no whole-WP mode.
3. The AI checks current Design and source state, searches all related documentation, collects the selected obligations, plans, implements, verifies, reviews and records the result. Nested sections belong to that one selected substep.
4. Inspect its [execution receipt](execution/README.md), PRs and actual gate evidence. Submit the next entry yourself. An open PR, missing published package or blocked external test is not silently treated as accepted.

Each copy block works in a fresh task with access to these files. You do not need to paste the full prompt again. The scope is one owning substep; the AI stops at its handover.

## Files

| File | Purpose |
|---|---|
| [list.md](list.md) | 447 ready-to-copy substeps in the formal serial order, spanning 51 active WPs |
| [reading-map.md](reading-map.md) | Common authorities, all current requirement/architecture/experience document paths, per-WP reading context and reference-source boundaries |
| [baseline.json](baseline.json) | Exact Design commit, corpus hashes, order/counts and reviewed external prompt hash |
| [execution/README.md](execution/README.md) | Durable implementation receipts for future runs; no implementation is accepted by preparing this plan |
| [tools/sync-plan.py](tools/sync-plan.py) | Standard-library generator/checker for IDs, titles, anchors, dependencies, copy blocks, paths and drift |
| [review.md](review.md) | Preparation scope, comprehensive review, corrections and evidence limits |

The reusable prompt is intentionally at `C:\MyFile\Projects\arcforges-implementation-prompt.md`, outside this repository, replacing the obsolete `arcforges.md` at the same parent directory. The Plan commit records its SHA-256, **not its contents**. Back up the prompt separately or explicitly bring it into a repository if versioned recovery is needed; this Plan commit alone cannot restore that external file.

## Baseline and maintenance

Preparation uses accepted Design commit `575ba9f929bcb2806e08b9776d9bdb7b0633358a` on `main`, verified against the remote. The authoritative schedule is `docs/planning/implementation-sequence.md` §9; numbering is an identity, not an execution sort key. All 51 `.90` gates are separate entries. WP20 is future-only and WP27/29 are retired. The optional letter/nested notation is supported by the prompt, but no extra identifiers are invented.

Run this read-only check after any local navigation/prompt change:

```powershell
python C:\MyFile\Projects\Plan\tools\sync-plan.py --check
```

If accepted Design changes, first verify the new Git baseline and review scope, dependencies, headings, new concrete authorities and the curated supplement map. Only then regenerate and review:

```powershell
python C:\MyFile\Projects\Plan\tools\sync-plan.py --write
python C:\MyFile\Projects\Plan\tools\sync-plan.py --check
```

The generator reads the clean current Design checkout and writes only Plan's `list.md`, `reading-map.md` and `baseline.json`. It does not fetch, switch, edit or commit Design, alter implementation repositories, or rewrite the external prompt. It intentionally fails on an unclassified new WP or structural inconsistency instead of guessing an order. Regeneration is not semantic approval: review the mapping and update `review.md` before committing. A matching hash does not establish that a referenced business design or runtime works.

Keep execution receipts and their accepted baseline history when regenerating navigation. Update one selected substep at a time. Current implementation evidence must remain distinguishable from historical source inventories, fixtures, real integrations and commercial activation.
