# Acceptance register

Real-world validation that cannot run at development stage, and the human prerequisites the plan depends on (R-TEST-003; ArcForges-Design `docs/decisions/AD-0014-delivery-method.md` §7–8).

**Rules:**
- An entry here is **never reported as proven** by a fake, an emulator or a simulation.
- A task with a deferred entry can reach `complete` for its development-stage scope once it has recorded what is possible now. The entry stays open until the real-world run happens.
- **Which prerequisites block.** Only the **Blocks** column of §2 decides:
  - a prerequisite that blocks a **task** (an implementation task's merge, or the activation steps of AF-PROD-01) sets that task `blocked` while it is missing (`python tools/plan.py set-state <task> blocked --blocked-by H-xx --reason ...`), and the plan continues with tasks that do not depend on it;
  - a prerequisite that blocks only **`complete`** leaves the task `delivered` until the evidence can be recorded;
  - every other prerequisite never blocks: the task uses its fakes or skips the leg with a stated reason.
- **Production prerequisites never block implementation.** Cloud and Web tasks deploy dark ([AD-0014](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0014-delivery-method.md) §9); production key material, domains, provisioning and publication approval are needed only by AF-PROD-01.
- Owners: **User**, meaning the product owner (human), or the named task, which prepares the procedure.

## 1. Deferred real-world validation

| ID | Validation | Why deferred | Prerequisites | Prepared by | Status |
|---|---|---|---|---|---|
| AR-01 | Fresh-machine install and first run: per-user setup program on a clean Windows 11 profile and machine (and its refusal on Windows 10); `install.sh` on bare-metal Linux | The workstation is not a clean machine | A clean Windows 11 machine or VM, optionally a Windows 10 VM for the refusal, and a bare-metal Linux host (user provided) | AF-DIST-01 | Open |
| AR-02 | Second OS account isolation: pipe DACL and socket permissions refuse another local user | No second account on the workstation (user decision 2026-10-10: never re-ask; procedure only) | A second Windows account and a second Linux uid | AF-DP-01, AF-NODE-01 | Open |
| AR-03 | Physical multi-machine LAN: DNS-SD discovery, pairing, placement and cache sharing across real machines | One workstation only | Two or more machines on one LAN | AF-LAN-01, AF-LAN-02, AF-LAN-03 | Open |
| AR-04 | Production code signing and reputation: Authenticode with the production certificate, SmartScreen, ES256 release manifest key, apt key | Signing custody is human | H-04 | AF-DIST-01 | Open |
| AR-05 | Real Paddle checkout, renewal, cancellation and refund with live webhooks | Payment provider account and real money flows | H-01, H-07; commerce activated (AF-PROD-01) | AF-COM-01 | Open |
| AR-06 | Real Google Play purchase on the internal testing track; live RTDN; acknowledgement | Play developer account and app listing | H-02, H-07, H-17; commerce activated (AF-PROD-01) | AF-CLD-07, AF-AND-03 | Open |
| AR-07 | FCM delivery to a physical Android device | Firebase project and a physical device | H-03 | AF-CLD-06, AF-AND-02 | Open |
| AR-08 | Android app on physical phones: camera QR, background behaviour, Play install | No device CI; physical devices are human-held | A physical Android phone; H-02 | AF-AND-01, AF-AND-02, AF-AND-03 | Open |
| AR-09 | Production cloud operations: alert routes, budget thresholds, the degradation ladder and essential-only mode, and Cloudflare budget alerts on the production account | Production configuration is owner-controlled | H-06, H-09; surfaces activated (AF-PROD-01) | AF-OPS-01, AF-PROD-01 | Open |
| AR-10 | Human screen-reader sessions (NVDA or Narrator on Windows, Orca on Linux, TalkBack on Android) | Human session required (user decision 2026-10-10: never re-ask; procedure only) | A person using assistive technology | AF-DESK-01, AF-DESK-02, AF-WEB-02, AF-AND-01 | Open |
| AR-11 | ARM64 hardware runs (win-arm64, linux-arm64) | No ARM64 host | An ARM64 Windows device and an ARM64 Linux host | AF-REPO-01 (builds), AF-ACC-01 | Open |
| AR-12 | Bare-metal Linux with headless lingering; other distributions (Ubuntu 22.04/24.04) and older systemd degrade paths | No bare-metal Linux host or other distribution is available | Linux hosts with those distributions | AF-EXEC-02 | Open |
| AR-13 | Package-manager and plugin publication: winget, Scoop bucket, apt repository, Claude Code marketplace, Codex plugin | Publication is outward-facing and needs accounts | H-04, H-05; user approval to publish | AF-DIST-02, AF-AI-02 | Open |
| AR-14 | Live transactional e-mail (account security notices) | Live mail excluded at development stage (user decision 2026-10-10) | H-19 | AF-ID-01 | Open |
| AR-15 | Real-world multi-day agent workload trial with Claude Code and Codex sessions in parallel on the workstation | User acceptance activity | The user's real projects | AF-ACC-01 | Open |
| AR-16 | Optional privileged features: Windows machine-wide service mode; Linux I/O control in a privileged native Linux install | Needs administrator or root installs by the user | User-performed privileged install | AF-DIST-01; AF-WSL-01 (superseded: its privileged WSL guest leg was dropped, ArcForges-Design AD-0018) | Open |
| AR-17 | Doctor host-posture check on a standard Windows account, and on a machine with Administrator protection switched on (Windows 11, security-baseline or device policy) | No venue offers a standard account (as for AR-02: the product owner's decision of 2026-10-10, second-account checks are procedure only and never re-asked), and none has Administrator protection switched on: it is off by default, and switching it on is a device policy change followed by a restart (Design verification register V-W08) | A user-provided Windows 11 machine or VM with a standard account and an administrator account, Administrator protection switched on (device policy and restart; not advised on Hyper-V devices, V-W08) | AF-DIAG-01 | Open |
| AR-18 | A Windows node identifies a running WSL VM's worker process (`vmmem` or `vmmemWSL`) as one `GUEST_VM` consumer in unmanaged load, never controlled, and never presents the VM's Linux processes as its own (ArcForges-Design 03 §1, §2, §9; A-L01, AD-0018 §2). Procedure: on Windows 11 with WSL2 and one distribution installed, (1) start the distribution outside ArcForges (`wsl -d <distro> -e sleep 600`); (2) run a native node; (3) `arcforges ps --label guest --json` lists the VM worker with label `PROCESS_LABEL_GUEST_VM`, no task, and a memory figure close to Task Manager's for that process, and no Linux process of the distribution appears; (4) allocate about 2 GiB inside the distribution (for example `python3 -c "b=bytearray(2<<30); import time; time.sleep(60)"`): `arcforges resources --json` shows unmanaged memory rising and the memory budget falling by about that amount within about 10 s; (5) a task running `wsl.exe -d <distro> -e sleep 30` has every process flagged `crossesVmBoundary`, and `ps --label managed` lists only Windows processes of its job; (6) run `ArcForges.ClosedLoop.Tests -method *ATaskThatRunsWsl*` there and keep the VM workers it prints | WSL is not installed on the workstation, so no VM worker runs there; the `crosses_vm_boundary` flag itself is proven with the inbox `wsl.exe` (AF-RES-01) | A Windows 11 machine with WSL2 and one distribution (user-provided; installing WSL is the user's step) | AF-RES-01 | Open |
| AR-19 | Successful Windows process adoption (ArcForges-Design 04 §10; `ResourceService.AdoptProcess`): a same-user process outside every job is adopted into the root job and a nested adoption job (the root job's limits apply, V-W01), appears as an `ADOPTED` task with label `ADOPTED`, its existing children follow, it can be terminated through `process.terminate`, and it ends `LOST` ("no exit status: the node is not the adopted process's parent") when it exits; after a node restart an adoption job the node cannot reopen (L-14) ends the task `LOST` through `container_missing`. Procedure: on a Windows 11 machine where a process created through WMI `Win32_Process.Create` is outside every job (check with `IsProcessInJob`), run `Node.Platform.Windows.Tests -method *AdoptionTests.AProcessOutsideAnyJobIsAdoptedWithItsChildrenAndTerminated` and `Node.Core.Tests -method *AdoptionLifecycleTests.AnAdoptedProcessThatEndsByItselfEndsItsTaskLostWithoutAnExitStatus` and `-method *AdoptionLifecycleTests.AnAdoptionContainerTheNodeCannotReopenAfterARestartIsLost`, plus `-method *AdoptionLifecycleTests.CancellingAnAdoptionJournalsStoppingBeforeItsFinalResult` (MR-105: real journal has initial RUNNING without previous states, exactly one STOPPING even after repeated cancellation, FINISHED CANCELLED/HAPPENED with no exit code, no adopted FINALIZING, and the shared kind-guarded model also checks an ordinary task); none may skip with the "already in a job" reason | On the workstation every user process, a WMI-created one included, is already in a job (ArcForges-Design register L-30), so 04 §10 refuses every candidate and the capability `adopt` reports `LIMITED`; the refusal path is proven there (AF-SEC-01) | A Windows 11 machine or VM where a WMI-created process is outside every job (user-provided) | AF-SEC-01 | Open |
| AR-20 | MR-07: establish the cause of the Windows supervisor test's unexplained node stop exit 75 and verify a discriminating repair if required | The historical failure has not recurred with the retained diagnostics; non-recurrence cannot establish its cause or prove a fix | A captured native Windows recurrence with verbose transport/descriptor/node/supervisor evidence, or a proven causal reproduction; the Windows MCP venue is already available, no new human provisioning | AF-NODE-01 | Open; unresolved observation, not a passed check or task block |
| AR-21 | MR-11: a non-elevated Windows node and an elevated client of the same user: user-SID pipe ownership succeeds, but an unidentifiable elevated peer is refused before API execution | Existing automated ownership tests do not create two processes at different integrity levels; owner deferred full end-to-end testing on 2026-10-15 (ledger 30) | User-performed Windows 11 cross-integrity run at final end-to-end acceptance; no automatic elevation or re-request now | AF-DP-01, AF-NODE-01 | Open; deferred validation, no task block |
| AR-22 | MR-15: establish the cause of the historical Windows crash-test all-sealed-values-unavailable observation and a discriminating repair if required | Original failure lacks the unsealing reason; current crash tests use isolated file-backed keys and cannot validate the historical Credential Manager path | Existing or naturally recurring nonsecret diagnostic, or separately owner-authorized causal evidence; MR-16 real-store cleanup/stress prohibition stays in force, no new real-store operation authorized | AF-NODE-02 | Open; unresolved observation, deferred validation, no task block |

## 2. Human prerequisites

| ID | Prerequisite | Needed by | Blocks | Notes |
|---|---|---|---|---|
| H-01 | Paddle seller account, products and prices for `pro_monthly` and `pro_annual`; webhook secret in Cloud secrets | AF-COM-01 (live only), AF-PROD-01 (commerce surface), AR-05 | Nothing at development stage (live runs: AR-05); `complete`, not delivery, of AF-PROD-01 (commerce stays off without it) | Development uses signed fixtures (`FakePaddle`) |
| H-02 | Google Play developer account, merchant profile, app listing, subscription product `arcforges.pro` (base plans `monthly`, `annual`), RTDN topic, Play Developer API service account | AF-AND-03, AF-PROD-01 (Play commerce), AR-06, AR-08 | Nothing at development stage (live runs: AR-06, AR-08); `complete`, not delivery, of AF-PROD-01 (Play commerce stays off without it) | Development uses `FakePlayDeveloperApi` |
| H-03 | Firebase project and FCM service account | AF-CLD-06 (live only), AF-PROD-01 (push surface), AR-07 | Nothing at development stage (live delivery: AR-07); `complete`, not delivery, of AF-PROD-01 (push stays off without it) | Development uses `FakeFcm` |
| H-04 | Signing custody: Authenticode certificate, ES256 release manifest key, apt GPG key, Android upload key | AF-AND-03 (release readiness), AR-04 | Nothing at development stage (test keys); production releases and AR-04 | Development, including AF-DIST-01, uses test keys that are never shipped |
| H-05 | Domains and DNS: `arcforges.com`, `releases.`, `relay.`, `status.` | AF-PROD-01 (publishing the site and profiles; relay and status endpoints), AR-13 | AF-PROD-01 only | Development uses the local stack, and implementation tasks deploy dark. Request it when AF-ACC-01 starts |
| H-06 | Cloudflare account settings: Containers enabled, budget alerts configured | AF-PROD-01, AR-09 | AF-PROD-01 only | The coordinator never changes account or security settings. Dark deploys need no flagship Containers. Request it when AF-ACC-01 starts |
| H-07 | Prices, currencies, trials and introductory offers | AF-COM-01, AF-CLD-07, AF-PROD-01 (commerce surface), AR-05, AR-06 | Nothing at development stage (`commerce.sales_open=false` until decided); `complete`, not delivery, of AF-PROD-01 (commerce stays off without it) | Until decided, `commerce.sales_open=false` |
| H-08 | Support response targets | AF-OPS-01 | Nothing (the default proposal applies) | Default proposal: Pro first response in 2 business days |
| H-09 | Monthly cloud cost ceiling | AF-OPS-01 (default budgets in development), AF-PROD-01, AR-09 | AF-PROD-01 (the production daily budgets are derived from it); nothing at development stage | `31 × (daily budgets + residual daily worst case)` stays within it (Design 14 §7.4) |
| H-10 | Legal texts: terms, privacy policy, refund policy, subprocessor list | AF-PROD-01 (publishing the public site; commerce needs the published legal pages) | `complete`, not delivery, of AF-PROD-01 (the public site and commerce stay off without it) | Production publication refuses placeholder text; AF-WEB-01 merges dark without them |
| H-11 | Tool installs that tests need, on the Linux verification host and on the Windows workstation (for example `gnome-keyring`, `cargo`, `cmake`, `sccache`, `ccache`, FASTBuild, the Visual Studio C++ tools for F-T06) | AF-DP-02, AF-TOOL-02, AF-LAN-03; AF-WSL-01 (superseded, ArcForges-Design AD-0018) | `complete`, not delivery, of AF-DP-02, AF-TOOL-02 and AF-LAN-03 when one of their F-items needs the tool | Installs are the user's (user decision 2026-10-10); the task lists the exact packages |
| H-12 | Repository settings changes (branch protection, environments, secrets) where a task needs them | Any | The task that names the change | The coordinator never changes repository security settings, except the required status checks of the conditional CI as the user authorized on 2026-10-16 (AD-0016 §2 names the change), and the `main` rulesets that require the host statuses as the user authorized on 2026-10-22 (AD-0020); never to get a PR merged |
| H-13 | Claude Code and Codex installed and signed in on Windows and on the Linux host | AF-AI-01, AF-AI-02 (F-A01, F-A02) | `complete`, not delivery, of AF-AI-01 and AF-AI-02 (Linux legs of F-A01 and F-A02) | Without them the Linux legs of the probes are skipped with a stated reason |
| H-14 | A clean Linux environment with `sudo` for the user (a fresh user or container on a Linux host), for `install.sh` and `.deb` install tests | AF-DIST-01 | `complete`, not delivery, of AF-DIST-01 (Linux install legs) | The task names the distribution and packages; installs are the user's |
| H-15 | One real logoff and logon on the workstation when the task asks, to verify the windowless supervisor start (F-N03) | AF-EXEC-01, AF-DIST-01 | `complete`, not delivery, of AF-EXEC-01 and AF-DIST-01 (F-N03) | Requested once per task, at a time the user chooses |
| H-16 | Production cloud key material generated and stored as Cloudflare secrets: command signing, entitlement token and relay HMAC keys, and a bucket-scoped R2 S3 API credential for presigned support uploads (a Node Issuing CA only with roadmap RM-01) | AF-PROD-01 | AF-PROD-01 only | Development uses test keys and dark deploys need none; the coordinator never handles key material. Request it, with H-05, H-06 and H-20, when AF-ACC-01 starts |
| H-17 | A Play-enabled Android emulator image signed in with a licence-test account | AF-AND-03 (optional real billing smoke), AR-06 | Nothing (optional) | Development uses `FakeBillingClient` |
| H-18 | Docker on the workstation (optional), for the Cloud repository's `test:container` diagnostics | AF-CLD-01 (optional) | Nothing (optional; never a gate) | Never a gate; the local cloud stack runs without Docker |
| H-19 | Transactional e-mail provider account (Postmark, with Amazon SES as fallback), sending domain with SPF, DKIM and DMARC records, and API credentials in Cloud secrets | AF-ID-01 (live only), AF-PROD-01 (identity surface), AR-14 | AF-PROD-01 (the identity surface sends sign-in codes and security notices); nothing at development stage (live delivery: AR-14) | Development uses `FakeMailSender` |
| H-20 | Approval to run the Cloud repository's provisioning script against the production account, creating the D1 database, the R2 bucket with its lifecycle rules and the Queue (or the user creates them and supplies their IDs) | AF-PROD-01 | AF-PROD-01 only | At Cloud `92ba1dc9` only the `proof` environment has these bindings; AF-CLD-01 writes and tests the script locally. Request it, with H-05, H-06 and H-16, when AF-ACC-01 starts |
| H-21 | A read-only Cloudflare GraphQL Analytics API token stored as a Cloud secret, for the daily billing reconciliation (Design 14 §7.5) | AF-OPS-01 (optional) | Nothing (optional; without it reconciliation reports off) | The user creates and stores it; the coordinator never handles it |
| H-22 | The Linux MCP server and its host (ArcForges-Design AD-0019 §1–3): a standard MCP server, usable by Claude Code and Codex alike, on an independent native Linux host (a VPS or another suitable Linux environment, never local WSL), with a systemd user manager, cgroups v2 delegation of `cpu`, `memory` and `pids` to the user, the repositories' pinned toolchains, Docker builds that reach NuGet without TLS interception, and a file channel from the workstation for Git bundles (AD-0019 §3; *amended 2026-10-22:* DesktopPlatform's native hand-off archive is withdrawn because, since DesktopPlatform PR #195, each leg builds what it verifies from the commit alone; *former text (kept as history):* "a file channel from the workstation for Git bundles and DesktopPlatform's native hand-off archive"; *amended 2026-10-22 by AD-0020:* no file channel is needed, since the host fetches each pushed commit from GitHub; it needs read access to the repositories on GitHub and `gh` with a credential that can write commit statuses, preferably `ARCFORGES_STATUS_TOKEN` limited to commit statuses) | Every Linux leg of every repository (AD-0019 §2), for example AF-RES-01 and AF-SCHED-01 | Delivery (the pre-push verification) of every push in a repository where AD-0019 has merged: with no Linux MCP server no Linux leg can be recorded, so the push is rejected (AD-0019 §5, §8). *Amended 2026-10-22 by AD-0020:* the merge of every PR into `main` instead, which needs the `arcforges/linux` status this host reports | Provisioned and configured by the owner, separately; no repository holds its address, client configuration or credentials. There is no transition venue: neither local WSL nor an agent's own sandbox substitutes. *Superseded 2026-10-21 (kept as history):* under AD-0018 the Claude Code Cloud Linux environment ran portable Linux legs and the owner's WSL Debian distribution served as the interim real Linux host |
| H-23 | The isolated Linux secret-store test host (ArcForges-Design AD-0019 §6): a test account or machine reached through the Linux MCP server, separate from the verification account, carrying the root-owned marker `/etc/arcforges/isolated-secret-store-test-host`, with a Secret Service provider (`gnome-keyring`, `dbus-daemon`, `secret-tool`, `dbus-send`) and the .NET SDK of `global.json` | The opt-in Linux Secret Service tests of the OS secret-store tier (DesktopPlatform; ArcForges's binding when delivered) | None for routine delivery: the tier is opt-in and outside the host verification (before 2026-10-22, the pre-push verification) | Provisioned by the owner. Replaces the `ArcForgesTest` WSL distribution; without the marker the tier runner refuses Linux |

## 3. Development-stage evidence to record per entry

When the prepared-by task finishes, it adds the following under the entry:
- the procedure (exact steps and commands);
- what was proven now: closed-loop tests and emulator or local runs, with links;
- the residual risk that only the real-world run removes.


### AR-20: MR-07 StopNode exit 75

This remains an unresolved observation, not a repair or a validation pass. The evidence and audit limits are in
[the MR-07 observation](maintenance/2026-10-25-mr07-observation.md). It creates no human prerequisite and blocks no task.

When a recurrence is observed during authorized maintenance:
1. Preserve the reviewed commit, binary paths, UTC times and the existing complete failure output before restarting anything.
   Inspect actual processes and completion markers after a timeout; do not reuse old PID or host-state assumptions.
2. Use the native Windows MCP. Keep the existing verbose StopNode trace, endpoint descriptor process identity/liveness,
   supervisor log and node log. Do not collect environments or credentials. The current fixture already records this failure context.
3. If a targeted reproduction is justified, use a matching Release build (locked restore/build once when needed), with no competing
   formal build/test, and one bounded batch that stops on the first failure. For the two original scenarios:
   `dotnet test --project tests/ArcForges.ClosedLoop.Tests -c Release --no-build --filter-method ArcForges.ClosedLoop.Tests.WindowsTests.TheSupervisorRestartsACrashedNodeAfterItsBackoff --filter-method ArcForges.ClosedLoop.Tests.WindowsTests.TheRegisteredAutostartCommandStartsTheSupervisorWhichStartsTheNodeWithoutAWindow --minimum-expected-tests 2 --output Detailed`.
4. Establish why the endpoint disappeared or the response was lost, with the recorded process identities and event order.
   Do not assign the old RECOVERING/INTERNAL race as the cause of the different pipe-missing exit 75 without evidence.
5. Close only with a proven cause and a discriminating regression/repair where required, reviewed and verified at its final pushed
   commit on the required native hosts. More silent runs alone never close this entry. No retry-count increase or weakened assertion.

### AR-21: MR-11 same-user cross-integrity client

Current development evidence: the user-SID ownership fix and three `PipeOwnershipTests` already exist in ArcForges main
`5eaee92a4a964469bad41dad28dad9787b7552cf`; the fix was introduced by `3c323b2` during AF-NODE-01. `OwnerIsUser` rejects another
user, BUILTIN\Administrators, SYSTEM and absent SIDs. A real user-owned pipe carries a byte after the owner check; a pipe owned by
the token's default owner is accepted only when that owner is the user. The retained Windows CI leg at reviewed head
`8fe744ffee80f24b59f835af60ba43e4a5163391` ran Client.Tests 102/102, no skips. This is existing evidence, not a new cross-integrity
run. No missing ownership test or source repair was found. DesktopPlatform's separate transport is MR-12, not resolved here.

The two checks differ: the client checks the server pipe's user SID; the node must also identify its peer. Current NodeClient turns
three dropped hellos into AccessDenied and explains that an elevated client of a non-elevated node is refused. A successful pipe
ownership test does not prove successful node Hello across integrity levels. This acceptance expects that refusal, not privilege
support or node elevation. The real pair remains unverified; the owner's ledger-30 deferral is retained without re-asking.

User-performed procedure at final end-to-end acceptance (not run in this maintenance pass):
1. Record the source revision, matching Release binary paths, Windows version and whether each shell is elevated. In an ordinary
   shell and then in the user's elevated shell run the already built ownership tests:
   `dotnet test --project tests/ArcForges.Client.Tests -c Release --no-build --filter-class ArcForges.Client.Tests.PipeOwnershipTests --minimum-expected-tests 3 --output Detailed`.
   Preserve the test output identifying the token-owner relation; both runs must pass all three tests without skips. The SID rule
   tests alone are not a substitute for the next two-process case.
2. In the ordinary shell prepare a unique temporary test root, its `config/node.json` containing a `dataRoot` inside that root, and a
   unique pipe name. Set `ARCFORGES_CONFIG_DIR` to that config directory, `ARCFORGES_ENDPOINT` to that pipe name and
   `ARCFORGES_TEST_MACHINE=isolated`; unset `ARCFORGES_OS_SECRET_STORE_TESTS`. Use `--test-mode` on every invocation, as the existing
   ClosedLoop TestNode fixture does, so the node data key uses the isolated file-backed store. Never select a real credential store.
   Run `<matching arcforges.exe> node run --test-mode` there. In another ordinary shell with the same three test-environment values,
   run `<matching arcforges.exe> node wait-ready --test-mode`, then `<matching arcforges.exe> status --json --test-mode` as baseline.
3. In the user's elevated shell set the same isolated test-environment values and no OS-store opt-in. Run
   `<matching arcforges.exe> status --json --verbose --test-mode` with a 30 s external bound. Preserve exit/stdout/stderr and the
   node log. Require the client ownership check to accept the user-owned pipe, then AccessDenied/refusal when the ordinary node
   cannot identify the elevated peer; no successful Hello, privileged API action, replacement node or elevation by ArcForges.
   If the OS permits peer resolution instead, preserve that evidence and review the stated expectation before closing this entry.
4. Re-run ordinary-shell status to prove the original node remains usable; stop it from that ordinary shell with
   `<matching arcforges.exe> node stop --test-mode`. Preserve process identities, endpoint descriptor and logs before disposing only
   this temporary environment. No managed privileged task, second account, device-policy change or real credential cleanup is needed.

Producer component check added by MR-12: DesktopPlatform's `LocalRpcPipeOwnershipTests` uses the same user-SID rule and explicit
user-owned parent-child and service listeners. Its current-token Windows run passed 4/4; this does not prove the elevated branch.
At final end-to-end acceptance, from a matching built DesktopPlatform checkout, in the ordinary and then the user's elevated shell,
set `ARCFORGES_LOCALRPC_OS_STREAMS=1` (never the OS secret-store opt-in) and run
`dotnet test --project src/BuildingBlocks/ArcForges.LocalRpc/Tests/ArcForges.LocalRpc.Tests.csproj -c Release --no-build --filter-class ArcForges.LocalRpc.Tests.LocalRpcPipeOwnershipTests --minimum-expected-tests 4 --output Detailed`.
Keep the token-owner relation printed by the tests and require all four tests to pass without skips. Unset that local opt-in afterwards.
This tests the producer in each token; only the separate ordinary-node/elevated-client procedure above tests the actual pair.
ArcForges' adoption of the producer version is MR-43. See [MR-12 evidence](maintenance/2026-10-25-mr12-validation.md).

Residual risk: no retained run proves the actual ordinary-node/elevated-client peer-resolution/refusal combination. Close only with
that two-process evidence and review of the observed result. AR-02 second-account isolation and the deferred positive auto-start leg
remain separate and open; this entry neither proves nor changes them.

### AR-22: MR-15 historical sealed-input loss

The historical Windows CrashConsistencyTests(420) observation remains unresolved, not repaired or validated.
[MR-15 evidence](maintenance/2026-10-26-mr15-observation.md) records the original PR, backend change, audit scope and limits.
The current file-backed isolated crash tests and their passing profiles do not validate the former real Credential Manager path.
No current task or maintenance dependency is blocked by this entry.

Procedure if existing evidence is supplied or a natural recurrence is observed during otherwise authorized work:
1. Preserve the original output and UTC times before retry/reset. Record the source/binary revision, test scenario, acknowledgement
   count, backend and isolation mode from existing diagnostics. Keep UnavailableReason and case outcome, never key/environment values.
2. Classify the actual diagnostic: unrecorded/missing/unreadable/wrong-length key, changed backend, purge, or authentication mismatch.
   An unavailable result alone proves none of these causes. Preserve the original relation between writer, kill and reopening reader.
3. Do not run the old concurrent Windows/WSL scenario, change assertions/retries, select a real OS store, set its opt-in, run its tier,
   list/read back/delete credentials or credential files, or start a real-store stress batch. MR-16 and the retained recovery proposal
   remain controlling. This procedure grants no additional host, credential or test authorization.
4. A real-store experiment would need separate explicit owner authorization and a reviewed isolated venue/procedure; do not request
   or start one automatically. Existing nonsecret evidence may instead establish the cause without such an experiment.
5. Close only with a proven cause, a discriminating regression and reviewed repair when required, and the owning repository's final
   pushed-head native checks. Additional silent or isolated passing runs alone never close this entry.
