# AFV2-MXC-01 — native cohort revalidation

Status: native author acceptance and independent source/evidence review passed;
final required repository checks and delivery are in progress. No task completion,
source merge or product profile admission is claimed at this checkpoint.

## Scope and decision

The isolated probe qualifies official Microsoft.Mxc.Sdk1.0.1/schema1.0.0 and
source fda29ac63bc306b7f97f3b86b4b63d44f7f40cf2 for native win-x64/linux-x64.
It adds no product runtime or Node.js dependency and removes no critical executor.
The user-approved local-process boundary is merged in Design73
(4bc1d2be8916a961d167b4965e30e45bc3023ef1) and Plan147
(da24652d090023a06175b1f43301b1fb0eaaaff5). Trusted host observation of explicitly
supplied inputs is recorded, not an independent rejection condition. Real secrets
remain excluded from ordinary logs and public/shared evidence; actual payload
isolation and implicit host-credential boundaries remain unchanged.
Historical8252c8f reports and the original failed verdict are preserved.

Design evidence PR74 subsequently merged as a877c184521fac493bb1066955992c598d68172a
from3b45fec917a551de68c5f028f1f5f0817101debf/treefb0ead82e946757487ff7669b5eb727877348deb.
Independent review and exact-head Windows4/4PASS63s / H22Linux4/4PASS29s preceded
that merge. Original Design logs are20261117-122801-3b45fec917a5-win and
20261117-122812-3b45fec917a5-linux. This records cohort acceptance separately from
pending Node delivery.

## Candidate and native evidence

Runtime source9a9378bc3a6bc8190d896ca7ef0e43eee5abd886/tree4b8785f999505582558c85019bdceb7b4952cf7e.
Final candidate d460524d7fa23e1558fc7ddd5e4a3c31e66e71d6 changes only the bounded
admission record and correct dual-RID locked-restore command after those runs.
Node draft93: https://github.com/ArcForges/ArcForges/pull/93.

Both actual designated hosts independently used their retained verified official
package/release inputs. Locked restore and Native AOT publish passed with zero
warnings/errors. Stage checks bind exact native members, license and upstream
SPDX; Windows has five actual Valid Microsoft signatures. No private upstream
build, loader override or fake native execution is used.

| Evidence | Windows DEKU | Linux H-22 |
|---|---|---|
| Probe SHA256 | ab9486fd2dd58cf8e6c9bc328f802aff66f64bdbd997c7012400e6065e7bf1ad | d3ff0a71a3a9614e360dbeb4011c8fee88268a74dfdf581bd8cc6b3e4218557c |
| Manifest SHA256 | dc0bfb3708e1994f1ddf5714a5bd30f8f7d0149af6ecf519d96c06271040a34c | 2a9df34d5e78d232ee81f5f4f7ed7b55052428eca61dc746281eddb7849ecf2a |
| Summary SHA256 | 9e1676addeedbbb465a4a0e0f1544220fc76a095db815075907167fd6355f12e | e499109bd69dd5476522c0fd1996a999e5dfdad745941c3aeea37a461dc9781b |
| Real runs | Five official-executor/Job-empty cases | Five rounds of pipe, PTY, Kill/Wait |
| Invalid-stage cases | Four fail before workload | Four fail before workload |

Windows originals: C:/MyFile/Projects/ArcForges/ArcForges/.worktree/afv2-mxc-01/artifacts/mxc-01/,
including windows-author-9a9378bc3a6b-revalidated-summary.json and per-run reports.
Linux originals: /home/sammiller/arcforges/ArcForges/.worktree/afv2-mxc-01-9a9378b-native/artifacts/mxc-01-native-9a9378b/summary.json,
with per-run reports and native build/stage/negative logs beside it. The experiment
ran as sammiller(uid1000) in user-unit arcforges-mxc01-9a9378b-121810, which exited0.
First-new-process and warm/idle measurements did not flush OS caches or prove
product performance targets. Service build memory is not probe idle memory.

Linux argv observations were four true and one false; no raw argv is exported.
The driver's additional casePidsAbsent field incorrectly reads a nonexistent key
and is excluded from evidence. Valid cleanup evidence is the probe's immediate
real processId absence assertion after each native wait and successful reports;
reviewer additionally observed all15 actual PID paths absent afterward. Original
summary/hash remain unchanged. No native rerun is needed for that auxiliary field.

## Review, recovery and remaining work

Independent nonauthor id_review read the complete11-file final difference and
original Windows/Linux hashes, stage members, reports and negatives; no blocking
source or native-author evidence finding remains. Final exact-head full profiles
remain incomplete: Windows15steps are rerunning with process-local English output
after the existing warning-count parser rejected a Chinese zero-warning summary.
H22Linux20steps recorded a genuine exclusive ResourceTests failure while waiting
for the fourth Normal task to enter Running, before pressure allocation. Focused
fixture/state diagnosis is in progress. Both use unchanged eng/verify.py
run-and-report; original failures remain preserved. No host result is copied or manually posted.

This probe migrates no data and changes no published package, applied SQL or
existing product executor. Rollback is rejection of this candidate; preserve old
inputs/evidence. Other RIDs and complete ConPTY/filesystem/network/Job/cgroup/
recovery compositions remain unqualified. No production activation or deployment.

Next resolve the required-check failure and finish fullchecks, merge reviewed Node93, then
record actual merges and complete MXC01 through plan.py. MXC02 is next eligible
only after real completion; existing user authorization covers ordinary delivery.
