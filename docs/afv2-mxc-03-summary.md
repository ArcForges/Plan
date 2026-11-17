# AFV2-MXC-03 — Linux qualification evidence

## Current delivery state

The complete H-22 native experiment and final repository host checks passed.
Node PR96 merged at `687eb3ad5d7f7b2e993d061df1dc5ccc96d13cb8`; Design PR76/77
merged at `6fa2a98ad3f93793134555320f0bd362e81625f0` and
`41d25327841e6c88df639bbcb387682bd067f7a1`. Plan checkpoint154 merged at
`fc96a516384b65130746b0b1b7a0255c2a4f9b89`; this completion-record change marks
MXC03 complete through plan.py, bringing the graph to9/40 after its own merge.
The later MXC04 admission decision and public activation remain separate.

Native source is `50e602a83ece2c4de75d8dbd32777c7833a6eaf7`; reviewed final
source `022946a305e505e5817162c79a956c7816b99b12` only formats Admission
initializers, preserving C# tokens/non-whitespace bytes and original evidence
identity. Final tree is `1b6fb25cbe65c6b0c1ba4f1b59e2734df32fef29`.

Final unchanged host profiles passed on that exact final commit:

- Native Windows deku:15/15 PASS2171s, original receipt
  `20261118-013632-022946a305e5-win`.
- H22 Linux:20/20 PASS2010s, original receipt
  `20261118-014327-022946a305e5-linux`; summary SHA256
  `c3a37cc950f630138fc0da571d51db14d1c18032befc407b1756cc793c7ce4b7`.

Receipts remain under each producing repository's `.git/arcforges-verify/logs`.
Both reporters automatically posted success. Actual strict required statuses,
latest CLEAN head and resolved threads were checked before normal merge.
Independent nonauthor source/native review is recorded on
[PR96](https://github.com/ArcForges/ArcForges/pull/96#issuecomment-6956376954);
[final host gates](https://github.com/ArcForges/ArcForges/pull/96#issuecomment-6956887604)
are recorded separately. All verification processes have exited.

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

The following original attempts are retained alongside the final passing checks above. Original50e Linux failed Admission
formatting, receipt20261118-005847-50e602a83ece-linux; the correction is022946a.
Original50e Windows passed15/15 in2190s, receipt20261118-005846-50e602a83ece-win.
Final022 Windows subsequently passed at20261118-013632-022946a305e5-win.

Final022 Linux receipt20261118-010502-022946a305e5-linux has an exclusive
CloudLink pressure-setup failure: only57 connections within3s against a required
value greater than256. The test and receiver source match actual Node main.
The reporter later exited after its SSH output stream had disconnected; no final
summary exists and its status was not reported as success. Preserve the failure
and incomplete receipt. Isolated bounded diagnostics passed with298 connections/Peak256/browser200 and
no premature producer exit; observed connect waits do not establish the original
packet-level cause. One unchanged original-method control passed1/1 in1.629s.
A single full unchanged022 formal retry passed20/20, with detached private output
logging; no threshold or assertion was relaxed. Both JIT and native CloudLink
groups passed36/36 in that full run. The original packet-level cause remains
unproven; this is not attributed to a host/network configuration defect.

Design e95476f passed independent review and both formal legs: H22 4/4 in31s,
receipt20261118-011411-e95476f531ca-linux; Windows4/4 in17s,
receipt20261118-013522-e95476f531ca-win. PR76 merged normally as
6fa2a98ad3f93793134555320f0bd362e81625f0. Plan now validates against that actual
Design main. A follow-up one-line register disclaimer fix, reviewed PR77, merged
as41d25327841e6c88df639bbcb387682bd067f7a1 after exact71017e9 Windows4/4 PASS74s
(receipt013951) and H22 4/4 PASS30s (receipt014149). It preserves the experiment
owner and all evidence while avoiding a second owner inferred from disclaimer
text by the reciprocal parser. This latest Design main is the Plan validation
baseline. Node final-head statuses subsequently passed and PR96 merged.

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

No ordinary publication or deployment applies: the existing Node workflows
have no main-push publication trigger. Final Node/Design merges and completion
are recorded through plan.py; sequence is regenerated. Finish this Plan record
against actual latest Design main, then continue eligible AFV2-MXC-02 using its
preserved draft and full current definition. Do not stop the authorized graph.
