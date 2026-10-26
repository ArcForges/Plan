# MR-18: own-job memory evidence and honest limit detail, 2026-10-26

MR-18 is fixed. [Design#37](https://github.com/ArcForges/ArcForges-Design/pull/37) merged first as
973934c658f62967be4b6cc40d0526d877ee4383. [ArcForges#58](https://github.com/ArcForges/ArcForges/pull/58) merged as
a4c1b2bf1b8afd0112fb490aa590c3ac8199ac96, final reviewed head15d6717144468ce0be615e8538f858d29b0fed7d,
treefed15ef1b4251c08d8bd48afcfe32b2530570e06, base852d23d8b4daca78cef509cb7a6925b18795b6b1.

## Repair and scope

MEMORY_LIMIT is a normalization of own-job evidence plus nonzero exit, not proof of memory causation or allocation refusal.
The old detail said the attempt reached its commit limit even when only the lower notification threshold had been crossed.
The new detail explicitly names the attempt's own job and that allocation refusal is not proven; raw exit/effect rules remain.

The old hard-memory packet branch latched MemoryLimitHit without checking the attempt's own limits. Confirm actual own-job
notification/peak or existing hard-limit peak evidence before latching, using one predicate shared with the holder so MR-17
durable evidence keeps exactly the same comparisons. Descendant usage is included in own aggregate usage, but a descendant's
lower cap is not the attempt cap. Queued packets after disposal fail closed on the expected disposed-handle path.
No scheduler/enforcement algorithm, enum/RPC/package/schema/migration or credential operation is changed.
AD-0005/date,04 section7 and internal contract comments state evidence scope/uncertainty.

Internal read-only packet observation and a borrowed real-port accessor support test provenance/composition. A test associates
actual jobs and observes kernel packets; it never posts a packet manually or calls the handler with simulated data. The borrowed
port remains owned by the platform. Production has no observer by default.

## Before evidence: separate discriminating failures from delivery prerequisites

Classification logic was unchanged in the baseline stages; read-only observation/composition seams were present.

- ab04206f2eb70a07bdd8808d5e765957e9d5ac8c: Core node-gap/detail cases3 failures+2 controls, no skips14.663 s,
  testexit2. Existing MemoryLimit reason/marker was correct but the detail lacked own-job scope and uncertainty.
- Three default/ordinary parent-forwarding experiments (mr18-before, before2, before3) timed out on the required packet-delivery
  precondition. With a separate child port, the child port captured real hard packet10; raw parent trace showed process packets,
  not the required hard packet. These are incomplete delivery experiments, not attribution failures, validation passes or proof
  that forwarding is impossible. No retry of them was counted as a repaired-code pass.
- cc6ddbacc709043cead8ddf951a569eae093ce4d (tree7d764d4f4391630c1c6f224c56a102aa728196f8), mr18-before4:
  explicit real shared-port composition with a key read from a real root process packet. Child29692 exited3762504530;
  nested peak110678016 bytes, attempt peak117784576 below own notification268435456 and hard402653184.
  The kernel delivered actual hard packet10 to the dispatcher and old own hit=True. Assert.False failed, no skips4.292 s;
  build0 warnings/errors12.01 s, testexit2/outer wrapper0. This is the discriminating scope failure.

The shared-port case is explicit and does not establish default-forwarding delivery on this host. No fake events, manually
posted packet, fake accounting value, asserted-unobserved success or weakened predicate/bound substitutes for actual delivery.

## Memory-code author evidence at fa6f836

Headfa6f83622c8a2634b59b069dbb124e525b83ffce/tree8778dc64a3340f3f2e93c8ded1798ddcfd380e13:

| Check | Native Windows | Native Linux |
|---|---|---|
| Format,Release build/analyzers |0 warnings/errors12.88 s |0 warnings/errors15.43 s |
| Own/detail regression | JIT5/5,no skips14.736 s; AOT holder5/5,no skips13.810 s | Windows behavior not inferred |
| Real shared-port nested packet | JIT1/1,no skips4.541 s; AOT holder1/1,no skips2.901 s | Windows behavior not inferred |
| TaskControl and JobTests |15/15 no skips76.477 s;8/8 no skips14.230 s | unchanged platform behavior |
| Repository guards |72/72,no skips3.292 s |72/72,no skips0.971 s |
| Pure format/protocol tests | full profile coverage |14/14,no skips0.597 s |
| Host Native AOT |0 warnings/errors42.37 s |0 warnings/errors47.89 s |
| Final diff/format/clean author wrapper |pass,exit0 |pass,exit0 |

The real node is in-process for the Core tests; AOT variants use the published holder, not a new standalone native-node
nested-dispatcher test. Jobs, allocations, queries, port and packets are real; external keys are isolated. The nested test
requires an actual hard packet and offers at most4 bounded real allocation opportunities for best-effort hard messages.
A suspended child's actual process packet is observed before it allocates. Fixtures clean only their own temporary data/jobs.

## Required-gate failure and necessary timing-isolation repair

The first Windows full-profile attempt at fa6f836 failed win-ci: SchedulerTests.TwoSessionsShareAdmissionsEquallyOnWindows.
The first12 starts were6:6, but slot-time share65.3948% violated the unchanged40–60% bound. Core322 total:283 passed,
38 platform skips,1 failed. Summary20261026-041700-fa6f83622c8a-win is false, wrapper1,120 s; later steps did not run.
This is not a final profile pass.

FairnessAsync uses300 ms holds but measures admission-to-finish slot time, including launch/finalization delays. Its comment
claiming independence from below-normal process startup was false; its two OS wrappers lacked exclusive isolation.
AGENTS explicitly requires timing/CPU-share-sensitive checks to use isolation=exclusive and DisableParallelization.
A single matching fa6f836 standalone diagnostic passed unchanged assertions:6:6 starts,50.5% share,10.048 s.
This supports the isolation diagnosis, not a proof about every possible source of timing variation.

Final delta15d6717 changes only both OS fairness isolation attributes and that comment. It changes no scheduler algorithm,
300 ms hold,12 tasks/session,5–7 first-start count,40–60% share assertion or180 s timeout. CI plus exclusive retains the same
tests, and both JIT/native exclusive gates run the timed check. git diff fa6f836..15d6717 -- src tools eng is empty.
The final-head Windows delta author passed format/build0 warnings/errors25.83 s, fairness1/1/no skips12.075 s,
6:6 starts/50.9% share,Repository72/72/no skips3.127 s,diff/clean wrapper0. Prior memory-code author results above are distinct
fa6f836 evidence, never presented as final-head statuses. The final full profiles below rebuilt/checked the actual final head.

## Linux orchestration recovery and old-head boundary

The initial fa6f836 Linux launch used a malformed compound background command and the MCP call timed out. Logs started,
but native process/PID-file inspection found the controller gone, no summary/exit and no residual compile/test processes.
Partial logs mr18-final.out/.err and summary directory20261026-121419-fa6f83622c8a-linux remain; no pass claimed.
A corrected standalone nohup run used mr18-final2 and the exact same candidate fa6f836. After the Windows failure required
a new head, that old Linux run was allowed to finish/clean private units normally. No user systemd manager was terminated;
no pkill -f,daemon-reload,assertion/step bypass or manual status report. The corrected old-head run completed all16 steps/1349 s,
wrapper0, summary20261026-121651-fa6f83622c8a-linux. Those fa6f836 results do not gate the new commit.
Final15d6717 uses mr18-final3 on both native hosts, with no competing same-host formal build/test.

## Final pushed-head gates, review and record

Design head27322c407f478ac4902bd82b1f547f394641e706/treea72f8ae2ff85c4a4e9ad85f36dfa80ce23b89032:
complete native Windows3/12 s,Linux3/44 s passed, all6 results/wrappers0 and required exact-head statuses read with fresh refs.
[Design review/gate](https://github.com/ArcForges/ArcForges-Design/pull/37#issuecomment-6408024200).
Design summary IDs20261026-040704-27322c407f47-win and20261026-120657-27322c407f47-linux.

Final source15d6717144468ce0be615e8538f858d29b0fed7d: complete native Windows13/1140 s and
Linux16/1382 s passed, all29 results/both wrappers0 and required engine-reported exact-head successes read;
owner-hosted checks/real OS-store tier skipped as expected. No old-head/partial pass or earlier author result substitutes.
Final summary IDs:Windows20261026-043314-15d671714446-win;Linux20261026-124013-15d671714446-linux. [Final source gate](https://github.com/ArcForges/ArcForges/pull/58#issuecomment-6408659480).
Author/review evidence and the timing diagnosis are linked from [source#58](https://github.com/ArcForges/ArcForges/pull/58).
Direct OpenAI Codex work/review alone under explicit user instruction; no other model/agent or independent reviewer claimed.

After actual source merge, Plan CLI appended one AF-EXEC-01 completion note and one AF-SCHED-01 gate-fixture note.
The MR-18 row, this evidence and the stop handoff are updated; no graph/task activation or later feature. MR-16 remains blocked and MR-07/11/15
remain unresolved/deferred. Latest owner instruction: finish MR-18 then STOP; MR-19 is next but unstarted.
Counts after this item:37 disposed,64 open,3 deferred,1 blocked of105;68 unresolved total.
