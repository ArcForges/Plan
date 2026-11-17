# AFV2-MXC-03 — Linux qualification evidence

## Current delivery state

The complete H-22 native experiment passed; repository delivery is still in
progress. AFV2-MXC-03 remains active and the graph remains8/40 complete. This
does not make the AFV2-MXC-04 profile-admission decision or activate a release.

- Node draft [PR96](https://github.com/ArcForges/ArcForges/pull/96), final source
  `022946a305e505e5817162c79a956c7816b99b12`.
- Native source `50e602a83ece2c4de75d8dbd32777c7833a6eaf7`; final source only
  reformats Admission initializers. Independent nonauthor review verified
  unchanged C# tokens and non-whitespace bytes. Original evidence is not relabeled.
- Design [PR76](https://github.com/ArcForges/ArcForges-Design/pull/76), candidate
  `e95476f531ca22b3ca3944bdaa56d7e26f9763bf`, records the exact cohort, original
  hashes, host/helper observations and measured overhead with its limits.
- Plan [PR153](https://github.com/ArcForges/Plan/pull/153) merged as
  `cf937ddc1c52778007bdc0980a1ae139c809d25f`; draft
  [PR154](https://github.com/ArcForges/Plan/pull/154) records subsequent qualification.

## Native result

The original full `linux-bubblewrap-sdk-v1` invocation ran on
`v2202601329473427941`, user `sammiller`/UID1000, through the owner-authorized
local `ssh netcup`. H-22 independently fetched the exact source and built/staged
the admitted official SDK1.0.1 cohort. No WSL, substitute host, root or host
network/security change was used.

| Group | Result |
|---|---|
| Admission |4/4 PASS|
| Terminal |17/17 PASS|
| Filesystem/policy |12/12 PASS|
| Network |10/10 PASS|
| Resource |13/13 PASS|
| Lifecycle/combined recovery |16/16 PASS|

All72 cases passed, all six groups confirmed cleanup, and the full command
returned0 in87.749s. The full receipt's source/embedded AOT identity is50e602a;
its Design/Plan invocation baselines are
`af28dc6378d91d678870abc628362476611efa32` /
`cf937ddc1c52778007bdc0980a1ae139c809d25f`.

- Full receipt SHA256:
  `57f41658b57c18ff350fde2a9afc428c9434946b1aa829735325336019288fcf`.
- Full driver events SHA256:
  `3b85f0b9475972bcdd6bb8bf6508ff7113f657493b79185556cfd3eb0bfe2d48`.
- H-22 originals:
  `/home/sammiller/arcforges/ArcForges/.worktree/mxc03-author-50e602a83ece/artifacts/mxc-03/`.
  Preserve `full-native-01.json`, its `.events.jsonl`, `full-native.log`,
  `author-summary.json`, build/AOT/staging logs and `full fixture 01/` child
  reports and owner logs. Private channel configuration/capabilities are not
  public evidence and must not be copied into GitHub.

The independent reviewer read the original same-host receipt and checked every
group report/event hash, actual stage-member hashes, pids/OOM counters and owner
results, missing-controller/no-owner evidence, actual200/CHDIR, both combined
scenarios, reconnect identities and held-cgroup cleanup proofs. Source and
native acceptance passed, including the final formatting-only delta.

Namespace-denial fault injection remains explicitly NOT_RUN under the protocol's
where-feasible clause. DNS records a bounded query's native refusal/no response,
without independent upstream delivery counts or a positive DNS claim. Stable
ingress/IPv6 restrictions remain; other hosts and later product/reboot acceptance
are not inferred from this experiment. Detailed measured performance definitions
and original values are in Design PR76; no new thresholds or cache-flush claims
were introduced.

## Repository gates and preserved failures

Required Node checks are not yet complete. The original50e Linux profile failed
only Admission whitespace checks, at
`20261118-005847-50e602a83ece-linux`; those source-only formatting changes became
022946a. Original50e Windows verification is finishing before its final-head
rerun, avoiding overlapping use of that repository's verification worktree.
The actual022946a Linux reporter is running with receipt
`20261118-010502-022946a305e5-linux`. A disconnected SSH output stream did not
stop it: reconnection verified its original process/worktree and continuing
same-host logs. Do not start another copy while it is alive.

Design e95476f has independent review and H-22 formal4/4 PASS in31s, receipt
`20261118-011411-e95476f531ca-linux`; Windows formal verification is pending.
Both repositories still require their actual final-head statuses before merge.
Plan must verify against the actual new Design main after Design merges.

Every original failed author report remains intact. Diagnosed corrections include
PTY foreground process identity, deleted cgroup proof, duplicate symlink mounts,
SDK refusal classification, final OOM sampling, pids-owner I/O initialization,
socket connect ordering, pressure-ready synchronization, and native pre-exec
failure observation. The068c701 cleanup=false report was not rewritten after a
read-only follow-up found its exact slice inactive; a later fresh run proved the
corrected held-cgroup cleanup path.

## Data, rollback and next action

This task adds the experimental probe and evidence only. It does not migrate
Node/Center data, remove the old Linux launcher/guards, change dependencies or
published bytes, deploy Cloud, or cut over the product runtime. Preserve the
original private fixture evidence. Any failed probe stops only its exact owned
unit/scope; unknown cleanup cannot be called successful or authorize deletion.

Finish the exact-head Node checks, merge reviewed Node and Design candidates
through normal rules, then record actual merge/publication applicability and
completion through `plan.py`. Regenerate sequence and validate Plan against the
latest Design main. Continue the next eligible authorized task afterward.
