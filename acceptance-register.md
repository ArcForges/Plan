# Acceptance register

Real-world validation that cannot run at development stage, and the human prerequisites the plan depends on (R-TEST-003; ArcForges-Design `docs/decisions/AD-0014-delivery-method.md` §7–8).

**Rules:**
- An entry here is **never reported as proven** by a fake, an emulator or a simulation.
- A task with a deferred entry can reach `complete` for its development-stage scope once it has recorded what is possible now. The entry stays open until the real-world run happens.
- Owners: **User**, meaning the product owner (human), or the named task, which prepares the procedure.

## 1. Deferred real-world validation

| ID | Validation | Why deferred | Prerequisites | Prepared by | Status |
|---|---|---|---|---|---|
| AR-01 | Fresh-machine install and first run: per-user MSI on a clean Windows profile and machine; `install.sh` on bare-metal Linux | The workstation is not a clean machine | A clean Windows machine or VM and a bare-metal Linux host (user provided) | AF-DIST-01 | Open |
| AR-02 | Second OS account isolation: pipe DACL and socket permissions refuse another local user | No second account on the workstation (user decision 2026-10-10: never re-ask; procedure only) | A second Windows account and a second Linux uid | AF-DP-01, AF-NODE-01 | Open |
| AR-03 | Physical multi-machine LAN: DNS-SD discovery, pairing, placement and cache sharing across real machines | One workstation only | Two or more machines on one LAN | AF-LAN-01, AF-LAN-02, AF-LAN-03 | Open |
| AR-04 | Production code signing and reputation: Authenticode with the production certificate, SmartScreen, Ed25519 release key, apt key | Signing custody is human | H-04 | AF-DIST-01 | Open |
| AR-05 | Real Paddle checkout, renewal, cancellation and refund with live webhooks | Payment provider account and real money flows | H-01, H-07 | AF-CLD-07 | Open |
| AR-06 | Real Google Play purchase on the internal testing track; live RTDN; acknowledgement | Play developer account and app listing | H-02, H-07 | AF-CLD-07, AF-AND-03 | Open |
| AR-07 | FCM delivery to a physical Android device | Firebase project and a physical device | H-03 | AF-CLD-06, AF-AND-02 | Open |
| AR-08 | Android app on physical phones: camera QR, background behaviour, Play install | No device CI; physical devices are human-held | A physical Android phone; H-02 | AF-AND-01, AF-AND-02, AF-AND-03 | Open |
| AR-09 | Production cloud operations: alert routes, budget thresholds, kill switches and Cloudflare budget alerts on the production account | Production configuration is owner-controlled | H-06, H-09 | AF-OPS-01 | Open |
| AR-10 | Human screen-reader sessions (NVDA or Narrator on Windows, Orca on Linux, TalkBack on Android) | Human session required (user decision 2026-10-10: never re-ask; procedure only) | A person using assistive technology | AF-DESK-01, AF-DESK-02, AF-WEB-02, AF-AND-01 | Open |
| AR-11 | ARM64 hardware runs (win-arm64, linux-arm64) | No ARM64 host | An ARM64 Windows device and an ARM64 Linux host | AF-REPO-01 (builds), AF-ACC-01 | Open |
| AR-12 | Bare-metal Linux with headless lingering; other distributions (Ubuntu 22.04/24.04) and older systemd degrade paths | Only WSL2 Debian 13 is available | Linux hosts with those distributions | AF-EXEC-02 | Open |
| AR-13 | Package-manager and plugin publication: winget, Scoop bucket, apt repository, Claude Code marketplace, Codex plugin | Publication is outward-facing and needs accounts | H-04, H-05; user approval to publish | AF-DIST-02, AF-AI-02 | Open |
| AR-14 | Live transactional e-mail (account security notices) | Live mail excluded at development stage (user decision 2026-10-10) | E-mail provider configuration (user) | AF-WEB-02 | Open |
| AR-15 | Real-world multi-day agent workload trial with Claude Code and Codex sessions in parallel on the workstation | User acceptance activity | The user's real projects | AF-ACC-01 | Open |
| AR-16 | Optional privileged features: Windows machine-wide service mode; Linux I/O control in a privileged guest install | Needs administrator or root installs by the user | User-performed privileged install | AF-DIST-01, AF-WSL-01 | Open |

## 2. Human prerequisites

| ID | Prerequisite | Needed by | Notes |
|---|---|---|---|
| H-01 | Paddle seller account, products and prices for `pro_monthly` and `pro_annual`; webhook secret in Cloud secrets | AF-CLD-07 (live only), AR-05 | Development uses signed fixtures |
| H-02 | Google Play developer account, merchant profile, app listing, subscription product `arcforges.pro` (base plans `monthly`, `annual`), RTDN topic, Play Developer API service account | AF-AND-03, AR-06, AR-08 | Development uses `FakePlayDeveloperApi` |
| H-03 | Firebase project and FCM service account | AF-CLD-06 (live only), AR-07 | Development uses `FakeFcm` |
| H-04 | Signing custody: Authenticode certificate, Ed25519 release manifest key, apt GPG key, Android upload key | AF-DIST-01, AF-AND-03, AR-04 | Tests use test keys that are never shipped |
| H-05 | Domains and DNS: `arcforges.com`, `releases.`, `relay.`, `status.` | AF-WEB-01, AF-CLD-04, AR-13 | — |
| H-06 | Cloudflare account settings: Containers enabled, budget alerts configured | AF-CLD-01, AR-09 | The coordinator never changes account or security settings |
| H-07 | Prices, currencies, trials and introductory offers | AF-CLD-07, AR-05, AR-06 | Until decided, `commerce.sales_open=false` |
| H-08 | Support response targets | AF-OPS-01 | Default proposal: Pro first response in 2 business days |
| H-09 | Monthly cloud cost ceiling | AF-OPS-01, AR-09 | Daily budgets are derived from it |
| H-10 | Legal texts: terms, privacy policy, refund policy, subprocessor list | AF-WEB-01 | Pages refuse a production build with placeholder text |
| H-11 | Package installs inside WSL2 Debian when a test needs a tool (for example `gnome-keyring`, `cargo`, `cmake`, `sccache`) | AF-DP-02, AF-TOOL-02 | Installs are the user's (user decision 2026-10-10); the task lists the exact packages |
| H-12 | Repository settings changes (branch protection, environments, secrets) where a task needs them | Any | The coordinator never changes repository security settings; the task states the exact change |

## 3. Development-stage evidence to record per entry

When the prepared-by task finishes, it adds the following under the entry:
- the procedure (exact steps and commands);
- what was proven now: closed-loop tests and emulator or local runs, with links;
- the residual risk that only the real-world run removes.
