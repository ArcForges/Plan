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
| AR-12 | Bare-metal Linux with headless lingering; other distributions (Ubuntu 22.04/24.04) and older systemd degrade paths | Only WSL2 Debian 13 is available | Linux hosts with those distributions | AF-EXEC-02 | Open |
| AR-13 | Package-manager and plugin publication: winget, Scoop bucket, apt repository, Claude Code marketplace, Codex plugin | Publication is outward-facing and needs accounts | H-04, H-05; user approval to publish | AF-DIST-02, AF-AI-02 | Open |
| AR-14 | Live transactional e-mail (account security notices) | Live mail excluded at development stage (user decision 2026-10-10) | H-19 | AF-ID-01 | Open |
| AR-15 | Real-world multi-day agent workload trial with Claude Code and Codex sessions in parallel on the workstation | User acceptance activity | The user's real projects | AF-ACC-01 | Open |
| AR-16 | Optional privileged features: Windows machine-wide service mode; Linux I/O control in a privileged guest install | Needs administrator or root installs by the user | User-performed privileged install | AF-DIST-01, AF-WSL-01 | Open |

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
| H-11 | Tool installs that tests need, inside WSL2 Debian and on the Windows workstation (for example `gnome-keyring`, `cargo`, `cmake`, `sccache`, `ccache`, FASTBuild) | AF-DP-02, AF-TOOL-02, AF-LAN-03 | `complete`, not delivery, of AF-DP-02, AF-TOOL-02 and AF-LAN-03 when one of their F-items needs the tool | Installs are the user's (user decision 2026-10-10); the task lists the exact packages |
| H-12 | Repository settings changes (branch protection, environments, secrets) where a task needs them | Any | The task that names the change | The coordinator never changes repository security settings; the task states the exact change |
| H-13 | Claude Code and Codex installed and signed in on Windows and inside WSL2 Debian | AF-AI-01, AF-AI-02 (F-A01, F-A02) | `complete`, not delivery, of AF-AI-01 and AF-AI-02 (WSL legs of F-A01 and F-A02) | Without them the WSL legs of the probes are skipped with a stated reason |
| H-14 | A second, clean WSL2 distribution with `sudo` for the user, for `install.sh` and `.deb` install tests | AF-DIST-01 | `complete`, not delivery, of AF-DIST-01 (Linux install legs) | The task names the distribution and packages; installs are the user's |
| H-15 | One real logoff and logon on the workstation when the task asks, to verify the windowless supervisor start (F-N03) | AF-EXEC-01, AF-DIST-01 | `complete`, not delivery, of AF-EXEC-01 and AF-DIST-01 (F-N03) | Requested once per task, at a time the user chooses |
| H-16 | Production cloud key material generated and stored as Cloudflare secrets: command signing, entitlement token and relay HMAC keys, and a bucket-scoped R2 S3 API credential for presigned support uploads (a Node Issuing CA only with roadmap RM-01) | AF-PROD-01 | AF-PROD-01 only | Development uses test keys and dark deploys need none; the coordinator never handles key material. Request it, with H-05, H-06 and H-20, when AF-ACC-01 starts |
| H-17 | A Play-enabled Android emulator image signed in with a licence-test account | AF-AND-03 (optional real billing smoke), AR-06 | Nothing (optional) | Development uses `FakeBillingClient` |
| H-18 | Docker on the workstation (optional), for the Cloud repository's `test:container` diagnostics | AF-CLD-01 (optional) | Nothing (optional; never a gate) | Never a gate; the local cloud stack runs without Docker |
| H-19 | Transactional e-mail provider account (Postmark, with Amazon SES as fallback), sending domain with SPF, DKIM and DMARC records, and API credentials in Cloud secrets | AF-ID-01 (live only), AF-PROD-01 (identity surface), AR-14 | AF-PROD-01 (the identity surface sends sign-in codes and security notices); nothing at development stage (live delivery: AR-14) | Development uses `FakeMailSender` |
| H-20 | Approval to run the Cloud repository's provisioning script against the production account, creating the D1 database, the R2 bucket with its lifecycle rules and the Queue (or the user creates them and supplies their IDs) | AF-PROD-01 | AF-PROD-01 only | At Cloud `92ba1dc9` only the `proof` environment has these bindings; AF-CLD-01 writes and tests the script locally. Request it, with H-05, H-06 and H-16, when AF-ACC-01 starts |
| H-21 | A read-only Cloudflare GraphQL Analytics API token stored as a Cloud secret, for the daily billing reconciliation (Design 14 §7.5) | AF-OPS-01 (optional) | Nothing (optional; without it reconciliation reports off) | The user creates and stores it; the coordinator never handles it |

## 3. Development-stage evidence to record per entry

When the prepared-by task finishes, it adds the following under the entry:
- the procedure (exact steps and commands);
- what was proven now: closed-loop tests and emulator or local runs, with links;
- the residual risk that only the real-world run removes.
