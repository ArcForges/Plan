# AFV2-MXC-01 — native cohort revalidation

MXC-01 is complete. Node PR93 merged
`b2ebace5c15a130b13a7dbd02fd9900e4983c6e8` from final candidate
`d460524d7fa23e1558fc7ddd5e4a3c31e66e71d6`; both trees are
`14c754b7da091eb4e0630fa2350d0a1dcde322bc`. Final source, original evidence and
all35 log hashes passed independent nonauthor review. Design final evidence PR75
merged `af28dc6378d91d678870abc628362476611efa32`; Plan PR148 carries the shared
completion record. Complete platform composition remains the subsequent tasks.

## Final required checks

| Host | Original directory under Node .git/arcforges-verify/logs | Result | Summary SHA256 |
|---|---|---|---|
| Windows DEKU |20261117-123248-d460524d7fa2-win|15/15 PASS,2102s|ec87c1c6b9413d6303993e663f4272782667ca8ca127ed89eea4f1f048fbe438|
| H22 v2202601329473427941/sammiller via ssh netcup |20261117-125046-d460524d7fa2-linux|20/20 PASS,1950s|089e7ca23191e06df55bc240ac10f06c547ad6411b42c511c57e96490b4ea8f1|

[Independent final review](https://github.com/ArcForges/ArcForges/pull/93#issuecomment-6939445328)
covered full source/native acceptance and these exact-head original receipts.
Ruleset24915109 remained strict with both successful statuses and no bypass actors;
review threads were empty. The merge tree matches. Actual main-push workflow query
returned zero runs, consistent with Node policy; no publication or deployment.

Design75 final candidate b050b8783d4832b7e7067ef149f64496bd671422 passed
Windows4/4 in16s and H22Linux4/4 in35s after independent evidence review; actual
merge af28dc6378d91d678870abc628362476611efa32 has tree139388ffcc5153be57b5cbe79889c6c56ef666ea.
Original Design logs20261117-132640-b050b8783d48-win and20261117-132700-b050b8783d48-linux.

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
the subsequently completed Node delivery recorded above.

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
original Windows/Linux hashes, stage members, reports and negatives; final source
and both required host profiles passed with no remaining blocking finding.

Prior failed verification remains preserved. Windows first full leg rejected a
Chinese zero-warning summary through the existing English-only parser; process-local
DOTNET_CLI_UI_LANGUAGE=en-US/VSLANG=1033 made the unchanged complete rerun pass.
Linux first full leg recorded a fourth Normal task Running wait timeout before
pressure allocation, then reached the aggregate exclusive900s bound. Its summary
SHA256 is c90b3f8812fd7562f1edd4acc04f4ba4da94bf83e34bd51fd193a87fa4457c0d.
The original admission cause is unknown; the fixture was disposed. A same-source
single-case diagnosis passed1/1zeroSkip19.476s, followed by fullR2 JIT/native pressure
cases and all20 checks. No source, assertion, timeout or CPU override changed.
The diagnostic apphost's earlier missing DOTNET_ROOT startup error is separate.
Original failures, diagnostic and both narrowly captured pressure fixtures remain
on H22; observer exited without touching test processes. No status was copied or
manually posted.

This probe migrates no data and changes no published package, applied SQL or
existing product executor. Rollback is rejection of this candidate; preserve old
inputs/evidence. Other RIDs and complete ConPTY/filesystem/network/Job/cgroup/
recovery compositions remain unqualified. No production activation or deployment.

Next complete the shared Plan148 merge against actual Design af28dc, then activate
MXC02 under existing authorization. The exact Program.cs/WindowsLauncher.cs scope
addition permits reusing the admitted entry/launcher for the already specified
Windows protocols; it adds no new product requirement or second runtime.
