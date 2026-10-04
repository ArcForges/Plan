---
task: GOV.07
status: delivered
recorded: 2026-10-04
claimant: w-c20261004-gov07
epoch: 1
---

# ArcScope policy tests consuming the shared policy engine

## Evidence

- Pull request: [ArcScope #23](https://github.com/ArcForges/ArcScope/pull/23), exact reviewed and merged head `0a9c2c053c3c1066029a032a4481e85b949ddef8` (independent approval comment on the PR, no blocking findings), merge commit `80dd7f24009a5259cf432551b26d70b634b7b746` on ArcScope main. Main-push CI run [37227084942](https://github.com/ArcForges/ArcScope/actions/runs/37227084942) succeeded: Workflow and secret checks (including the hosted architecture gate), CodeQL (C# and actions), Native win-x64, win-arm64 and linux-x64, Verify, Publish portable release and Verify publication. Provider job status only; no downloads. The hosted run on the PR head also passed all checks.
- Host: `tests/ArchitectureTests` (package-free, AGPL) imports the engine of the published `ArcForges.Build.Policy` 1.0.0-ci.94.1 (GOV.06 candidate, DesktopPlatform `d6e3fab`). The central pin moved from ci.20.1; only that coordinate changed in the five existing project locks (contentHash `PCpeEXik...`, nuspec SHA-256 `bd85acc0...`). Supporting set: solution entry, licence row, dependency policy and review reseal (history kept), provenance successor `gov-07-provenance-tools-r1` with inventory and regenerated NOTICE, pin text in README and build-identity docs, empty `eng/policy/exceptions.json`, `ci.yml` wiring. ArcScope is AGPL-3.0-only so there is no RP-03 exception; no Gitleaks or scanner configuration changed.
- Hosted wiring: the existing `quality` job now runs, after the full-history Gitleaks scan, a locked build, `naming_evidence.py` and then the hosted gate over the real SDK-compiled graph, with RP-01, RP-08 and RP-09 bound to the exact commit, run and attempt. Job timeout raised from 10 to 30 minutes (same precedent as GOV.05).

### Per-rule fixture table (positive passes, negative fails, shared engine)

| Obligation | Rules and fixtures |
|---|---|
| WP-05.00 layering | AT-01 (domain to infrastructure; application to UI; package layer roles), AT-02, AT-03, AT-04, AT-05, AT-06, AT-09, AT-10, AT-11 (negative), AT-14 (foundation and design system), RP-07 AOT fence; each with an allowed and a violating graph |
| WP-05.01 licence boundary | RP-02 (mismatched, missing SPDX, missing boundary, unclassified package), RP-03 (direct, transitive and package Apache-to-AGPL), allowlist from `reuse-policy.json` over the real admitted packages (permissive, exact ArcForges AGPL, non-ArcForges AGPL, GPL-only, unknown licence, wrong boundary), inventory equals the solution, exception inventory exact/owned/expiring |
| WP-05.02 forbidden terms | Canonical scanner from the exact published `ArcForges.Contracts.Validation` 1.0.0-ci.205.1 (identity checked at acquisition, two assets extracted); ArcScope scan 0 findings; 1 positive and 6 negative fixtures (one per forbidden term); hosted gate re-reads the report bound to commit, run, attempt and the pin |
| WP-05.03 generated-client consumption | Exact central contract pins, no sibling source or binary reference, no authored proto or client generation, no hand-written wire type, gRPC client, descriptor or marshaller, binary gRPC-Web only, registered compile-time JSON metadata, reflection JSON off in the AOT executable; each with a negative fixture |
| WP-05.04 banned APIs | One allowed and one banned compiled fixture for each of the seven categories in each of ArcScope's Domain, Infrastructure and UserInterface roles (provider calls are permitted only in the Infrastructure adapter role) |
| RP-01/RP-08/RP-09 | Missing, stale and failing evidence each rejected per rule |

## Honest limits and the deferral that keeps this task `delivered`

- **Executable production rules are deferred.** The engine fails closed with "Unresolved invocation cannot be audited" on the unmanaged function-pointer calls in `src/ArcForges.ArcScope/NativePackageProof.cs`, so the AOT executable is classified `Production: false`. Its banned-API scan, public-API test binding and production-only layer rules are therefore not enforced; layering, licence, AOT-fence and contract-consumption rules still cover it. The reviewer's mutant (adding `.Wait()`, `Type.GetType` and a `double` price to the executable) passed the hosted gate, while the same code in Core was caught. Only review enforces the executable until the repair lands.
- **Self-expiring.** A fixture and `VerifyDeferredExecutableScanIsStillBlocked` fail once the engine can audit that file, which forces `Production: true` to be restored.
- **Follow-up repair (open, not done, not claimed).** In `BannedSymbolScanner.Scan` (DesktopPlatform, `src/Build/ArcForges.Build.Policy/Architecture`) handle an invocation whose symbol is null and whose operation is a function-pointer invocation instead of throwing (about five lines plus positive and negative fixtures; size S). It needs a planning repair, a DesktopPlatform change, a new Build.Policy publication and then pin moves in ArcScope, Contracts and Cloud with their receipts. No task adding production code to the ArcScope executable should land before that repair. Until it merges, this task stays `delivered`; `complete` needs the repair or explicit user acceptance of the deferral.
- RP-10 binds every public production API to one host fact: a structural correspondence, not per-method coverage (disclosed in the PR body and code; as in the Contracts host).
- Reviewer mutants not run (the build slot was busy): layering, public native pointer, and RP-07 suppression with a resealed review. Five mutants and the baseline ran. The review and the author share one GitHub account.
- Not exercised: the host RP-07 properties on the executable itself beyond `IsAotCompatible`; Linux and macOS runtime beyond hosted Ubuntu CI; no local reproduction of the published-package naming download (the local scan used the same scanner sources).
- Substitutes still in use: none.
