---
task: NAT.15
status: superseded
recorded: 2026-10-08
claimant: w-deku-20261008-plan-1
epoch: 0
---

# Pdf family: real PDFium (chromium/8044) build admission, binding and real-parser containment acceptance

## Superseded 2026-10-08

Superseded by NAT.31 and NAT.32 under P2-022 (retirement of native in-app PDF preview and local PDF parsing). NAT.15 is retired, not completed: NAT.31 composes the still-image parsers into the ContentSandbox helper, PLT.45's completion edge moves from NAT.15 to NAT.31, and NAT.32 removes the PDF engine.

No NAT.15 delivery or completion is recorded in this ledger. DesktopPlatform pull request 154, "[NAT.15] Deliver real admitted PDFium parser and production composition input", was merged on 2026-10-06 (merge commit `24feb447955e131bcfbf3483d295af913d15d629`) and then discarded from DesktopPlatform `main` by the user’s reset of 2026-10-07: that merge commit is not an ancestor of `main` (checked 2026-10-08), so no NAT.15 work is on `main`. It is reference only and is not evidence of NAT.15 completion.
