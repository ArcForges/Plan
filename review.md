# Implementation prompt and sequence review

Reviewed on 2026-09-18, in one main context without subagents.

## Scope and baseline

The requested deliverable is a reusable single-substep implementation prompt and a complete linear navigation list. This is not product implementation, a replacement Design, or a renewed family-wide design audit.

- Accepted Design: `575ba9f929bcb2806e08b9776d9bdb7b0633358a` (`main`, merged PR12), checked against remote main before preparation.
- Formal authority: current decisions through P2-014, requirements, architecture/contracts/data-model, experience, planning and assurance.
- Preparation searched 170 tracked Markdown files (including repository instruction/entry files), excluding deprecated-input bodies. It extracted all active WP sections and citations, read the planning/producer authorities and relevant concrete profiles, and inspected the source sequence's exceptional ordering and staged obligations. This does not claim a fresh manual semantic audit of every paragraph in the 4.7 MB Design corpus.
- Plan began as a local Git repository with no commits and no files other than `.git`. No prior review folders were reconstructed.
- The existing root `arcforges.md` was read, renamed and rewritten as `C:\MyFile\Projects\arcforges-implementation-prompt.md`.
- Formal Design, primary implementation checkouts and all reference sources remain unmodified by this task.

## Collection and unified plan

Collection established **51 active WPs, 447 owning substeps and 158 dependency edges**. Each active WP includes a separate `.90` stage gate. WP20 is future-only; WP27/29 are retired. Source headings have no current letter-suffix or nested numbered substeps, but the prompt preserves that ownership convention for applicable future definitions. Missing numbers are not generated.

The former prompt was obsolete: old roots and monorepo assumptions, superseded runtime/protocol rules, a whole-step mode, invocation/function terminology, old absent reference files and a special commit policy. It was replaced coherently rather than patched around contradictory rules.

The unified solution is:

1. One reusable external prompt with a brief current product background, exact locations, single-substep boundaries, mandatory fresh Design searches, bounded collection/plan/implementation/review and honest evidence handover.
2. One generated `list.md`, using the actual formal topological schedule and the source's owning-section order. Every block supplies actual values; no invocation placeholder needs editing.
3. A `reading-map.md` combining citations from the **whole WP**, including appended bindings, with additional concrete authorities. The catalogue covers every current requirement/architecture/experience file; common assurance authorities and applicable historical evidence are distinguished.
4. Durable execution receipts for future work, separate from static navigation. None is marked accepted at preparation time.
5. A standard-library generation/drift checker and a baseline/hash record; local Plan commit after review.

## Review findings and corrections

| Issue addressed | Final treatment |
|---|---|
| An agent might treat the template as a function or switch to whole-WP mode | Prompt is direct execution guidance. Only one exact `ArcForges Substep NN.MM[A]` can be selected. |
| Explicit WP input tables omit useful concrete authorities | Whole-file citations plus targeted supplements include assistant and Android UI, native platform/degradation profiles, deployment/rollback, derived stores, extension/policy schemas and event/bridge semantics. Fresh searching remains mandatory every run. |
| Numeric sorting would corrupt the schedule | Derive WP order from implementation-sequence §9; preserve 42.11 before 42.10 and 43.07 before 43.06. Preserve the 53.06 gap and final 50.90. |
| The list could overreach into siblings or future producers | Read the full parent WP for obligations, implement only the selected owner and nested sections. `.90` is separate. Reading a downstream reference does not authorize implementing it. |
| Early package/fixture proof could be confused with product integration | Stage-specific reading notes and prompt examples retain actual producer order and named replacement gates. Scoped contributions do not prematurely close shared gates. |
| Generalizing gRPC-Web could replace legitimate protocol exceptions | Review clarified that designated authentication callbacks, object transfers and provider/internal exceptions retain their specified protocols. |
| Generic prerequisite prose could force unnecessary full release checks | Distinguish direct graph dependencies and previous substeps within the WP from mere linear-list adjacency and future shared-gate triggers. |
| Another conversation might lack prior implementation evidence | Use exact per-substep receipts with source/artifact identities and Accepted/awaiting-evidence/Blocked states. Preserve resumable history; do not assume an open PR or missing receipt is acceptance. |
| Root prompt is outside the local Git repository | Record the external path and exact SHA; explicitly state that a Plan commit does not version or restore the prompt contents. |
| A future source heading format might disappear from generation silently | Checker rejects unsupported owning-heading shapes and unclassified new WPs rather than silently omitting them. |

No product rule was invented to resolve a Design conflict. WP titles are retained from their source files, including the awkward current WP49 file heading `Web companion Companion`; the exact substep IDs/titles and file/anchor resolve unambiguously. This cosmetic source wording was not changed in Design.

## Structural verification

| Check | Result |
|---|---|
| All active formal owning sections appear exactly once | PASS — 447/447 copy blocks, no duplicates |
| Exact substep ID, title, source path and explicit anchor | PASS — compared independently with formal headings/anchors |
| Full direct dependency graph | PASS — all 158 edges precede their consumers; WP headers match source graph |
| WP and integration-gate coverage | PASS — 51 active WPs, 51 separate `.90` entries |
| Future/retired IDs and numeric holes | PASS — no WP20/27/29 execution; no invented 53.06 |
| Non-numeric orders | PASS — 42.11 < 42.10; 43.07 < 43.06; 47 < 45; 52 < 31/32/49; 50 last |
| Formal references in active WPs | PASS — cited files exist and all non-WP Markdown targets appear in the reading map or common context |
| Current requirement/architecture/experience catalogue | PASS — all files included as search surfaces |
| Generator drift check | PASS — `python C:\MyFile\Projects\Plan\tools\sync-plan.py --check` |
| Checker rejection probes, entirely in memory | PASS — rejects sibling substitution, a removed copy block, a changed owning path and a missing linked target |
| Obsolete execution instructions | PASS — removed old invocation fields, function/whole-step modes, old roots and superseded stack instructions |
| Old file ambiguity | PASS — former root `arcforges.md` no longer remains as another editable prompt |

An independent extraction of every formal owning heading was compared with every copy block, rather than relying only on the generator to validate its own expected output. The graph was also rechecked against each WP's upstream header. These checks prove navigation consistency at the recorded baseline, not semantic completeness of the product specification.

## Semantic walkthroughs

The walkthroughs inspect prompt behavior against the cited formal stage and selected section. They do not execute the implementation tasks.

| Selected scenario | Expected behavior confirmed by review |
|---|---|
| 00.00 / 00.90 | Authority/rights work can finish without inventing a future package or Cloud manifest prerequisite. Other WP00 substeps are not pulled into 00.00. |
| 03.05 | Read all concrete schemas, operation scopes, numeric/origin profiles and late completeness bindings; produce full language/package closure, without requiring future business handlers. |
| 06.07 | Prove the actual minimal Android/CF transport path; do not implement the later full companion or count a schema fixture as device evidence. |
| 08.00 / 11.09 | Private child transport and restricted fixture-parser isolation stay within their owners; no sibling-app hub or future parser dependency. |
| 13.05 / 13.15 | Common declarations/layouts precede family bodies and real packaged export acceptance. The first substep is not blocked by exports assigned to later substeps. |
| 17.00 / 17.04 | Complete selected UI behavior with explicitly allowed fixtures, retaining real producer/replacement obligations at WP23–26/52. |
| 42.11 / 42.10 | Preserve source order and technical commerce scope; actual payment/payout activation remains separately gated. |
| 43.07 / 43.06 | Actual provider evidence precedes the coverage-closure step; deterministic recorded fixtures remain a distinct evidence class. |
| 45.09 → 31 → 32 | Real push sender exists before complete companion/device distribution acceptance. Sender success alone is not a physical receipt. |
| 47 → 45 | Public Web tooling exists before Operations UI. Early fixture content does not become public pricing/download truth. |
| 50.90 | Requires all currently due real joined evidence; cannot call a green document checker a production release. |
| Resume, already-done work and Design drift | Recheck exact IDs, commits and evidence. Preserve prior work; do not repeat it or auto-advance. Material authority drift blocks dependent work until resolved. |
| External account/toolchain/hardware missing | Record the exact gate and needed evidence; continue only independent authorized work within the selected substep. Do not manufacture a pass or implement a sibling to hide the blocker. |

## Evidence limits and handover

This review establishes a coherent prompt and navigation mapping at the recorded Design baseline. No product code was built, published, deployed or tested; no AOT, native, Cloudflare, physical-device, browser, provider, payment or commercial gate was closed. Source/reference roots were located, not freshly audited as implementation deliverables.

`--check` deliberately detects later prompt/document/navigation drift. Before accepting regeneration, recheck the accepted remote Design, update the curated map for any new scope, review the generated diff and record a new review. Each implementation run must still search current related documents beyond this prepared map.

The next selectable task is **00.00 — Product and naming freeze**. It has not been started by this preparation task.

Reviewed external prompt SHA-256: `6bd05f047ce81e6904a3221e5824747bcd02c3614e776c6a2c7859b2fec296e8`.

## Final filesystem verification

All 1,125 local Markdown links/fragments resolve. Copy fences and explicit anchors are balanced/unique, the final prompt hash matches the baseline and review record, and generated/support files use UTF-8 without BOM and LF. The first format check detected a CRLF line in the generator; it was normalized and the affected checks passed on rerun. Design HEAD and remote main were rechecked at `575ba9f929bcb2806e08b9776d9bdb7b0633358a`, with the Design primary checkout clean. Plan has no remote; its delivery commit is local only.
