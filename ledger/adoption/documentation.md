# Adoption documentation reconciliation

Owner: ADOPT.11, w-20260927-adoc, epoch 1. Frozen inputs: [ADOPT.01 baseline](baseline.md), merged Plan `293d53d51e69`; Design source `722e85641c8a`.

## Findings and disposition

- Existing corpus audit at the frozen Design revision: 225 Markdown documents, 22,516 links, 6,816 definitions, no link/definition errors or missing stable anchors. The earlier 26 link errors are historical, not current blockers.
- Strict occurrence classification initially failed on a stale `invariant-coverage.md` line hash. [Design PR 70](https://github.com/ArcForges/ArcForges-Design/pull/70) repairs current rule citations and exact occurrence contexts: 133 unchanged records, 33 stale records removed, 28 newly reviewed exact records. The resulting strict classifier passes 161 records covering 165 occurrences. Reserved/retired allocation numbers and historical labels do not become active requirements. No blanket exclusion or checker weakening was added.
- NAT.05 now names the two retained probes and NAT.06 the retained native families/unchanged image ABI identity, matching current WP13 and cleanup authority. GOV.18 now names the exact required current inventory documents, affected rejection fixtures, and new same-owner reuse provenance while preserving historical receipts.
- The user's 2026-09-27 network instruction is reflected consistently: diagnose transient failures, bounded backoff, inspect possibly successful writes before retrying, never change proxy/network settings, and request intervention only for indispensable manual login/credentials.
- GOV.18 still owns the retired graph-validator migration and actual policy export repin. GOV.14 retains broader specification/decision-coverage acceptance. Passing corpus/classification checks do not certify the full legacy exporter or product acceptance.

## Validation and status

After repair, the existing corpus audit reports 225 documents, 22,569 links, 6,816 definitions, zero errors and zero missing anchors; strict classification passes 161 records/165 occurrences. `delivery.py generate` and `check` explicitly named retained roots `C:\MyFile\Projects\Plan\.worktree\adopt-11` and `C:\MyFile\Projects\ArcForges-Design\.worktree\adopt-11`: 436 tasks, 50 slices, 99 current views, zero warnings, valid ledger. No product build, public artifact download or runtime validation was performed.

Slice status remains authoritative in individual merged [task records](../tasks) and `delivery.py status/ready`; this reconciliation does not copy a rapidly stale whole-stage completion table. At the frozen baseline only ADOPT.01 was complete. Parallel slices add their own reviewed records and inherited task evidence. The generated task list is regenerated from the graph, never manually edited. Further exact worker scope findings are reconciled through reviewed graph changes; no product obligation is removed.

PR review and merge identities are recorded in the ADOPT.11 task claim and final task ledger receipt after the paired documentation changes merge.
