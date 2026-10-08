---
task: GOV.30
status: complete
recorded: 2026-10-09
claimant: w-deku-20261008-gov-30
epoch: 1
---

# Remove osx RIDs from the desktop RID set and owned lock and policy data

## Evidence

- Implementation: DesktopPlatform PR [#174](https://github.com/ArcForges/DesktopPlatform/pull/174) was reviewed and merged at head `cfd9c33b1f995c591fa3f013957671e00e306a3a` as `6b84ca17f6be64f69107dc3172ac9879ed510dcb` on `main` (`--merge --match-head-commit`, integration role `integration:DesktopPlatform` held by `w-deku-20261008-coord`). The approved head `b839e63b` merged main after NAT.32 (#172). `cfd9c33b` then merged main again after GOV.32 (#173), a clean merge that adds no manual change.
- Review: independent reviewer session `w-deku-20261008-rev-gov-30`.
  - Round 1 at `abc014bb` requested changes: the static osx scan was not committed, and the policy-data regeneration was not evidenced. Fixed in `6abb1e2e`.
  - Round 2 requested changes: the merge order was not met. Fix `4af9860d` made the reconciliation generator accept the rows NAT.32 already retired. Main, including NAT.32, was then merged in at `b839e63b`, and the receipt was re-chained to `nat-32-r1`. Under brief section 10, re-chaining an unmerged receipt is allowed in DesktopPlatform.
  - Round 3 at `b839e63b` approved. This approval is labelled review:GOV.30:r1 in workflow journal wf_a6f9b145-7d1.
  - The merge head `cfd9c33b` was then verified: its diff from `b839e63b` equals the GOV.32 delta line for line, and the gates pass.
  - The approvals are PR comments from one GitHub account, so independence is by session only.
- Planning authority: [P2-023](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/phase-2-specification-decisions.md#rule-p2-023). The `current.json` carve-out was added in Design PR [#341](https://github.com/ArcForges/ArcForges-Design/pull/341) (merge `318e49735ffb1453d7bd63e0589ed1b6c34d0dc0`), with coordinator adjudications in brief section 10.
- Outcome:
  - **Desktop RID set:** `eng/build/desktop-rids.props` is now `win-x64`, `win-arm64` and `linux-x64`. `linux-arm64` is not added.
  - **CMake:** the osx configure, build and test presets are removed from `CMakePresets.json`.
  - **Locks:** the osx sections are removed from the five owned locks (ContentSandbox, ContentSandbox Fixture, LocalRpcAotTests, ReleaseArtifactTests GrpcWeb and Realtime). Together the five locks differ from their predecessors only by 160 removed lines, with no additions, and each passes `--locked-mode`.
  - **Policy data:** the `runtime.osx-*` ILCompiler admissions are removed.
  - **Receipt:** the successor receipt `eng/policy/dependency-reviews/gov-30-r1.json` is chained from `nat-32-r1` through the committed generator `eng/verification/create_gov30_dependency_receipt.py`, and names reviewer `w-deku-20261008-rev-gov-30`.
  - **Reconciliation:** the osx runtime directory rows are removed through `eng/verification/create_gov30_reconciliation.py`, which reproduces the committed files byte for byte.
  - **Static scan:** `eng/test_desktop_rids.py`, run in the PR gate.
  - **Kept:** the shared fail-closed macOS refusal and the shared Unix-socket code; the immutable review, provenance and patch records; and the two `current.json` osx nativeRuns rows (osx-arm64 and osx-x64) of the ArcScope candidate `0.1.0-ci.8.1` entry, as immutable history. `eng/test_desktop_rids.py` exempts exactly these two rows. The GOV.30 task text and brief section 10 say 'the five published ArcScope prereleases'; that wording is inaccurate for `current.json`, which holds osx rows for that one candidate only. The task text correction is queued for the next planning batch.
  - **ADP-07 supporting bindings:** `.github/workflows/pr-gate.yml` (the scan step), `eng/test_desktop_rids.py`, the `eng/policy/reconciliation/source.json` count, and the `eng/provenance/files.json` rows for the new files.
- History unchanged: the recorded histories of GOV.17, PRF.04, PRF.05, PRF.06 and PLT.19 are not edited.
- Candidate identity: main-push [Publish NuGet run 37854886174](https://github.com/ArcForges/DesktopPlatform/actions/runs/37854886174) (run 129, attempt 1) on `6b84ca17` succeeded, with preflight passing. It published the DesktopPlatform cohort `1.0.0-ci.129.1`; its publish job log shows 17 'Your package was pushed' lines. Package hashes and registry receipts were not captured. This is the provider status, and nothing was downloaded.
- Obligations: P2-023, a governance obligation. The macOS desktop RIDs and their lock and policy data are retired, and no macOS support or validation is claimed.
- Validation actually performed:
  - **Hosted PR gate run [37846277058](https://github.com/ArcForges/DesktopPlatform/actions/runs/37846277058) at `cfd9c33b`:** 22 of 22 checks passed. That includes the static scan step, policy, provenance, reconciliation, licence and runtime, plus the native and managed-package jobs.
  - **Round 3 reviewer at `b839e63b`:**
    - dependency policy passed (58 NuGet coordinates, 10 Python tool dependencies, 281 inputs);
    - unit suites OK: `test_dependency_policy` (22), `test_desktop_rids` (11), `test_reconciliation` (8) and `test_licence_boundary` (12);
    - reconciliation passed (307 directories);
    - `check_provenance` passed (978 files, 140 records), and `native_provenance` passed (21 components);
    - the in-memory regeneration of the reconciliation files matches byte for byte.
  - **Round 3 reviewer, WSL2 Debian (kernel 6.18.40.1-microsoft-standard-WSL2), SDK 10.0.400, on a Linux-native git-archive copy (P2-024):**
    - locked restore and Release build with 0 warnings for the affected projects;
    - full-solution `dotnet restore DesktopPlatform.slnx --locked-mode` passed for 53 projects;
    - ContentSandbox tests: 97 passed, 1 failed (see untested coverage) and 9 skipped.
  - **Merge-head verification at `cfd9c33b`:**
    - `check_provenance`, `dependency_policy`, `reconciliation`, `design_policy` and `test_desktop_rids` pass, with their unit suites `test_dependency_policy` (22), `test_reconciliation` (8) and `test_design_policy` (21);
    - under SDK 10.0.400, `dotnet restore DesktopPlatform.slnx --locked-mode` passes, as stated in the PR #174 review comment; the run's host is not recorded;
    - ContentSandbox tests: 110 run, 101 passed, 0 failed, 9 skipped.
- Substitutes still in use: none introduced or removed.

## Untested coverage (stated expressly)

- `InvocationTests.AHelperThatDiesEndsTheInvocationWithATypedFailure` is intermittently flaky: it sometimes answers `capacity.busy` where `resource.parser_failed` is expected. It failed once in the round 3 WSL run and once in five isolated reruns. It is pre-existing, because no ContentSandbox source differs from main in this change. It passed in the merge-head run and in hosted CI. The receipt's statement that the test run passes is only intermittently true. The flake has a tracked owner note in the coordinator log.
- The 9 opt-in OS isolation tests were skipped.
- `licence_boundary --evaluate-managed` was not run in round 3. Hosted CI passed it.
- The RP-01, RP-08, RP-09 and AT-09 architecture evidence is hosted-only.
- macOS residue outside GOV.30's write scope, carried to the next planning batch under P2-023:
  - `tests/LocalRpcAotTests/README.md` lines 23-25 still describe macOS peer-PID support;
  - `tests/LocalRpcAotTests/Program.cs` prints 'PASS: Linux SO_PEERCRED and macOS SOL_LOCAL/LOCAL_PEERPID dispatch' (line 52) and keeps the Darwin dispatch (lines 31-32 and 1269-1281) as shared Unix-socket code.

  These are not a macOS validation. No macOS run exists.
- No macOS run exists or is claimed (P2-017, P2-023).
