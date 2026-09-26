# Execution ledger

The ledger records the execution state of delivery tasks. Together with the Design delivery graph and the record branches it determines readiness (`python tools/delivery.py ready`, which reads the merged `main` only). It holds no design authority: task definitions, prerequisites and obligations live in the Design graph.

Every ID has one key, in lower case with dots replaced by hyphens (`CON.02` → `con-02`, `ADOPT.03.contracts` → `adopt-03-contracts`); Git for Windows cannot store a ref or file named `con.02`.

## Claims, leases and roles

Records are branches, not files on `main`: `claims/<key>` for a task or adoption slice, `leases/<key>` for an exclusive resource (`leases/res-cloud-deployment`) and `roles/integration-<repository>` for a repository integration role (`roles/integration-contracts`). Each commit holds one `claim.json`:

```json
{
  "schema": 1,
  "kind": "task",
  "id": "CON.02",
  "claimant": "w-host-20261001-1",
  "epoch": 1,
  "state": "claimed",
  "claimedAt": "2026-10-01T08:00:00Z",
  "updatedAt": "2026-10-01T12:30:00Z",
  "leaseUntil": "2026-10-02T12:30:00Z",
  "handoff": {
    "repository": "Contracts",
    "branch": "task/con-02",
    "worktree": "C:\\MyFile\\Projects\\ArcForges\\Contracts\\.worktree\\con-02",
    "host": "WORKSTATION",
    "prs": ["https://github.com/ArcForges/Contracts/pull/41"],
    "head": "<full SHA of the last pushed commit>",
    "reviewed": "<full SHA of the approved head>",
    "merges": [],
    "done": ["descriptor records and fixtures"],
    "next": ["await review"],
    "validation": ["generate --check clean; C#/TS conformance offline"],
    "blocker": null,
    "note": null
  }
}
```

- `kind` is `task`, `lease` or `role`; a lease also names the holding `task`.
- `state` is `claimed`, `blocked`, `released`, `delivered` or `complete` for tasks, and `claimed` or `released` for leases and roles.
- `leaseUntil` is a UTC time with a timezone while claimed or blocked, and null otherwise.
- `handoff` is the durable handoff record (Design DLV-40). The claimant updates it at each checkpoint described in [arcforges-implementation.md](../arcforges-implementation.md#durable-handoff).

Records are written only with `tools/delivery.py` (`claim`, `update`, `release`), each as a compare-and-swap on the record commit that was read. Only the claimant at the current epoch renews, updates, blocks, releases or completes a record. A re-claim after release, a takeover after the recovery checks and a completion follow-up append the next epoch. Branches are never deleted or force-updated: they are the audit trail of ownership. Repository administrators may add a ruleset that blocks deletion and non-fast-forward updates of `claims/*`, `leases/*` and `roles/*`. An unreadable or invalid record keeps its item unavailable until a reviewed fix repairs it.

## Task records

One file per task, `ledger/tasks/<key>.md` (for example `ledger/tasks/con-02.md`), added through a reviewed pull request titled `[<TASK-ID>] Record <summary>`:

```markdown
---
task: CON.02
status: complete
recorded: 2026-10-01
claimant: w-host-20261001-1
epoch: 1
---

## Evidence
- Pull requests (implementation, documentation, ledger), each with its reviewed head commit and merge commit:
- Published candidate identities (package, version, hash, registry receipt) and the CI and publication runs:
- Obligations satisfied (substep or package obligation and part):
- Validation actually performed (CI checks, local runtime checks with environment identity):
- Substitutes still in use and their removing tasks:
- Untested coverage:
- Remaining completion prerequisites and next action (delivered only):
```

`status` is one of:

- `delivered`: the outcome is merged and published, and a completion prerequisite is still open;
- `complete`: its own acceptance is satisfied and every completion prerequisite has a `complete` or `inherited` ledger record;
- `inherited`: satisfied by reviewed existing work during adoption;
- `superseded`: replaced by a recorded planning change.

Keep exactly one front-matter block per file. When a delivered task completes through its follow-up, or a task is superseded, edit the existing header in place and append the new evidence below it. Bundled tasks that share a pull request keep separate records.

`python C:\MyFile\Projects\Plan-B\tools\delivery.py check --plan <Plan worktree> --design C:\MyFile\Projects\ArcForges-Design-B`, with the Design primary checkout at current `main`, validates every record in the named Plan working tree: its front matter, file name, known task, status, uniqueness and satisfaction of completion prerequisites for `complete` records. Always name both roots; without `--plan` this command checks the Plan primary checkout instead of your change ([Planning and ledger changes](../arcforges-implementation.md#planning-and-ledger-changes)). The tool refuses to compute readiness from a ledger that fails these checks.

## Adoption records

`ledger/adoption/baseline.md` holds the frozen adoption inputs. Each adoption slice is recorded as `ledger/tasks/<slice key>.md` (for example `ledger/tasks/adopt-03-contracts.md`) with `status: complete` and one classification row per task in its scope. Every task the slice classifies as inherited, including each accepted-baseline task in its scope, gets its own `ledger/tasks/<key>.md` with `status: inherited` in the same pull request, so it never becomes ready; the other tasks of that lane in that repository become eligible under the normal dependency-readiness rule when the records are merged. Before editing, workers must read their classification and later adoption adjustments, reuse inherited evidence and, for inherited-with-adjustment tasks, implement the recorded remaining scope. Unresolved conflicts or blockers still stop the affected task and must be recorded in its claim; readiness does not resolve them. `ledger/adoption/<repository>.md` holds each repository's facts and combined classification table, and `ledger/tasks/adopt-nn.md` records the repository adoption task when all of its slices are complete. Their format and rules are defined in the Design [adoption stage](https://github.com/ArcForges/ArcForges-Design-B/blob/main/docs/planning/delivery/adoption.md). At introduction, no adoption record existed and the historical baseline was complete through WP03.02; WP03.03 had not started. Current progress comes from the merged ledger and record branches, not this historical statement.
