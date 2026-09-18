# Substep execution receipts

No implementation receipts exist when this plan is prepared. The list's 447 entries are pending work, not completed work.

For each actually selected substep, create or update a file named by its exact ID, such as `00.00.md`. Use one file per owning substep, including its nested sections. A letter suffix is retained when the formal identifier has one. Do not create empty files for future entries.

A receipt is a concise implementation/evidence record, not another task definition. It must be usable by a later fresh AI task without relying on chat history.

Record:

- Exact ID/title and formal owning file/anchor; time and one status: **Accepted**, **Implemented — awaiting specified evidence/integration**, or **Blocked**.
- Accepted Design commit; Plan/navigation baseline; source repository roots, starting and resulting commits, worktrees/branches, dirty-state limitations and any resumed earlier attempt.
- Documents/rules actually consulted and fresh searches performed beyond the initial map; relevant external official sources and verification dates. State any drift or unresolved authoritative conflict.
- Direct prerequisites and their receipts/artifact identities. If external work already satisfies a prerequisite, identify independently verifiable evidence rather than relying on a verbal claim.
- Obligation → changed implementation/artifact → test/scenario → observed result. Include the selected substep's completion gate and applicable WP-wide obligations, without claiming sibling gates.
- Exact commands/results and evidence locations. Keep document/schema/unit/fixture checks, isolated package consumers, actual runtime/provider/device tests and commercial activation in separate fields. Mark inapplicable evidence explicitly; unavailable evidence is not a pass.
- Producer/consumer source commits, release versions/hashes, relevant runtime/RID/OS/device/provider identity, and candidate/publication/manifest status. No secret values belong here.
- Commit and PR links for each changed owner; unresolved merge/publication/integration needs; local Plan commit carrying the record. The containing Git commit can identify the receipt itself; do not create a self-referential commit hash update loop.
- Required follow-up or external blocker, affected gate and evidence needed; any permitted later fixture-replacement owner. Give the next list entry only as navigation, with no automatic execution.

The first entry within a WP checks its direct upstream WP closures. Later entries also check earlier substeps within that WP. Source presence or a green generic CI run does not establish package availability, real consumer execution or gate acceptance. Cross-repository substeps have one consolidated receipt pointing to separate owner commits and artifacts.

A shared gate can remain pending at its named later trigger while this substep contributes accepted scoped evidence. Conversely, a required current gate cannot be moved later by changing the receipt. A `.90` receipt assembles the WP stage's evidence against compatible candidate identities; it cannot overwrite failed earlier evidence with a summary claim.

Update the same receipt on resumption, preserving material prior failures and the evidence that resolved them. Revalidate only what a changed input, failure or unresolved concern affects. Commit reviewed Plan receipt changes locally; do not upload the local Plan repository as part of an implementation PR.
