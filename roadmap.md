# Roadmap

The canonical TODO list and roadmap for ArcForges. ArcForges-Design [AD-0015](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0015-direction-editions-roadmap.md) §9 governs it; the Design product definition §10, this repository's README and AGENTS.md link here. No other backlog exists: an item that is not committed delivery lives here and nowhere else.

## Tiers

| Tier | Meaning | Where |
|---|---|---|
| **Committed delivery** | Release 1: decided, specified and scheduled | The tasks of [delivery-graph.json](delivery-graph.json), in the order of [sequence.md](sequence.md). This file does not repeat them. |
| **Accepted future work** (`RM-*`) | A product decision exists, but the work is not scheduled. It is never implemented before promotion (§4). | §2 |
| **Exploratory ideas** (`EX-*`) | Needs evaluation before any commitment | §3 |

## 1. Committed delivery (release 1)

- **Tasks:** every task in [delivery-graph.json](delivery-graph.json) (milestones M0–M15), in [sequence.md](sequence.md) order:
  - M0–M10 build the free local and LAN product;
  - M11–M13 build the cloud services: account and support for every user, and remote access, mobile monitoring and notifications as Pro;
  - M14 is operations and the release candidate;
  - M15 is production activation.
- **Product scope:** the Design product definition:
  - §5 editions: local and LAN free, cloud services in Pro;
  - §9 the operations release 1 manages end to end, and the gaps it reports.
- **Rule:** release 1 keeps its essential core behaviour and meaningful acceptance criteria. Fakes replace only unavailable external systems, never the behaviour being delivered (Design 16 §2).

## 2. Accepted future work

| ID | Item | Purpose | Why deferred | Prerequisites | Revisit when | Foundations in release 1 | References | Status |
|---|---|---|---|---|---|---|---|---|
| RM-01 | Account-based LAN trust and cloud discovery hints | Machines of one account trust each other and find each other across subnets without pairing each pair | Pairing already gives full LAN function for free. Account trust adds Node Issuing CA custody, revocation and a cloud dependency to LAN. | Identity and enrollment (AF-ID-01, AF-CLD-02); key custody (H-16 extension) | Team administration (RM-07) is promoted, or users with many machines report pairing as a burden | Reserved contracts: `IssueNodeCertificate`, `GetLanHints`, `ReportLanEndpoints`, `PEER_TRUST_ACCOUNT`; `fleet_node_certificate` table | AD-0008, AD-0015, R-LAN-002, AF-LAN-01 | accepted |
| RM-02 | LAN sharing of dependency caches (NuGet, npm, Cargo, pip) | Download each package once per LAN | A registry proxy needs its own integrity, authentication and upstream-semantics design | LAN placement and compiler-cache sharing delivered (AF-LAN-02, AF-LAN-03) | Per-attempt package counts across nodes, and download sizes where tools report them (Cargo, pip), show repeated downloads worth the work | `CacheUsage` and `Attempt.downloaded_bytes` per attempt; cache reports | R-CACHE-007, R-REC-006, AF-CACHE-01, AF-LAN-03 | accepted |
| RM-03 | Managed FASTBuild remote workers and other distributed-compilation backends | Use idle LAN machines inside one build | Worker deployment, trust and resource accounting need a design of their own | LAN placement (AF-LAN-02); FASTBuild adapter (AF-TOOL-02) | Users run FASTBuild or sccache-dist farms on their LAN | `-dist` use observed and labelled; peer offers and policies | R-TOOL-006, AF-TOOL-02 | accepted |
| RM-04 | Result-cache restore (RESTORE mode for PURE tasks) | Skip re-running deterministic tasks whose inputs did not change | Few tasks are asserted PURE now that retry classes are asserted, not inferred; restores need proven action keys | Result cache OBSERVE mode (AF-CACHE-01) | OBSERVE data shows frequent would-be hits with stable action keys | OBSERVE mode; `RESULT_CACHE_MODE_RESTORE`, `CACHE_RESTORE` attempts and `CACHE_RESTORED` reserved | AD-0006, AF-CACHE-01 | accepted |
| RM-05 | MCP over a local HTTP transport | Serve MCP clients that cannot spawn a stdio process | Every supported client uses stdio; an HTTP listener adds authentication surface | MCP adapter (AF-MCP-01) | A supported client needs HTTP, or remote MCP clients become a goal | The adapter's transport abstraction | AD-0003, AD-0004, AF-MCP-01 | accepted |
| RM-06 | Hosted history (Pro) | Keep, search and compare execution history across machines beyond each node's retention | Cloud storage cost, privacy and redaction review; release 1 keeps records on nodes | Records and exports (AF-REC-01); the cloud platform (AF-PLAT-01) | Pro users ask for cross-machine history, or team administration needs it | Correlated records and redacted JSON Lines exports | AD-0015, R-REC-003, R-REC-006 | accepted |
| RM-07 | Team administration (Pro or Team) | Organizations, members, roles, shared policies and team audit | Needs an organization model in identity and per-seat commerce | Identity (AF-ID-01, AF-ID-02); commerce (AF-COM-01) | Teams ask to manage shared machines and policies | Account audit; the policy document model | AD-0011, AD-0015 | accepted |
| RM-08 | Resource-demand and duration prediction beyond operational-memory statistics | Better admission, ETAs and placement from observed workloads | Needs real usage data first | Operational memory (AF-DIAG-01); correlated evidence (AF-REC-01) | Records show estimate errors that cost admission or placement quality | Operational-memory facts (p90 peak, duration), timelines, input fingerprints | R-MEM-001, R-REC-006, AF-DIAG-01 | accepted |
| RM-09 | Real-time resource requests from AI clients | Agents ask for capacity and get a grant or an honest wait, against actual capacity | Clients have no resource-negotiation protocol yet | Admission and explanations (AF-SCHED-01); MCP adapter (AF-MCP-01) | MCP or a client gains a resource-request mechanism, or agents need guaranteed capacity | Resource hints in `TaskSpec`, `ExplainTask`, MCP `queue_status` and `resources` | R-AI-001, AF-SCHED-01, AF-MCP-01 | accepted |
| RM-10 | Advanced disk-space analysis and lifecycle management | Cross-repository duplicate analysis, scheduled lifecycle policies and predictive cleanup | Release 1 delivers safe analysis and two-phase cleanup first | Managed storage (AF-STOR-01) | Disk reports show recurring reclaimable waste that manual cleanup misses | Storage analysis, cleanup plans, quarantine, disk records | R-STOR-007, AF-STOR-01 | accepted |
| RM-11 | Additional execution and integration adapters | More toolchains (for example Gradle, Maven, Go, Bazel) and more AI clients | Release 1 covers the measured priorities; each adapter needs real verification | Adapter contract (AF-TOOL-01) | Records show heavy commands that fall to the generic adapter, or users ask for a client | Published adapter manifests (`ListAdapters`); the generic adapter's records | R-TOOL-004, AF-TOOL-01 | accepted |
| RM-12 | Managing operations clients start outside their shell tool | Bring MCP servers, language servers and IDE tasks that clients launch under the same control | Needs client cooperation or launch-time interception that clients do not offer | Hooks and sessions (AF-AI-01) | A client offers a launch hook, or bypass evidence shows large unmanaged load | Bypass detection and coverage reports | R-AI-006, R-AI-011, AF-AI-01 | accepted |
| RM-13 | Shared .NET build servers across attempts (Roslyn compiler server, MSBuild server) | Faster repeated .NET builds by reusing warm compiler and build servers between attempts | A server shared between attempts runs one attempt's compiles in another attempt's container: the first build starts it, it is charged to that build and dies with it, and every later build finds it by pipe name (Design V-T09). No documented setting scopes it to one attempt | A verified per-attempt scope for the servers, or accounting of their work per caller; the .NET adapter (AF-TOOL-01) | Records show compiler start-up dominating .NET build time, or the .NET SDK offers a server scope per caller | Build servers off in managed executions; per-attempt phase timings and process records of the compiler; the reserved policy field `dotnet.shared_build_servers` | AF-TOOL-01, R-TOOL-005 | accepted |
| RM-14 | Dedicated lightweight helper executables (Windows attempt holder, Linux disk guard) | Lower per-attempt and per-user memory than the roles of the one multi-role binary | The product owner chose architectural simplicity on 2026-10-16: the holder and guard stay roles of `arcforges` (AD-0003), with targets set from measurements (Windows holder ≤ 10 MB, Linux guard ≤ 12 MB; Design 15 §2) | A second signed binary per platform, its update and packaging path (AF-DIST-01) | Measured per-attempt overhead becomes a real constraint, for example many concurrent attempts on memory-limited machines | Helper roles behind a narrow command-line contract (`node exec-wrap`, `node guard`), so a separate executable can implement them unchanged | AD-0003, Design 15 §2, AF-EXEC-01, AF-EXEC-02 | accepted |

## 3. Exploratory ideas

| ID | Idea | Purpose | Why not now | Prerequisites | Question to answer | Revisit when | References | Status |
|---|---|---|---|---|---|---|---|---|
| EX-01 | Plugin ecosystem and marketplace (integrations, cache backends, diagnostics, adapters) | Let others extend ArcForges without forking it | No plugin can yet be shown to stay inside the core permission, execution, resource and recording mechanisms; release 1 has no runtime plugins | A stable adapter contract (AF-TOOL-01) and the additional adapters of RM-11 | Can out-of-process plugins run entirely under the core mechanisms, with signed distribution? A marketplace never implies charging for local functionality. | A design shows that no plugin can bypass the core, and the adapter backlog (RM-11) shows demand | AD-0015 | exploratory |
| EX-02 | Hosted build and dependency caches as a cloud service | Reuse build results and downloads across networks, not only on one LAN | Cost and trust model unknown; LAN sharing comes first (RM-02) | Cloud budgets (AF-PLAT-01); LAN sharing results (AF-LAN-03, RM-02) | Is a cloud cache worth its cost and trust model compared with LAN sharing? | Measured cross-network cache demand and a cost model inside the Pro budget | AD-0009, AD-0015 | exploratory |
| EX-03 | GPU and accelerator scheduling | Bring local model inference and GPU builds under the same admission and enforcement | No measured contention yet, and no portable GPU enforcement design | Resource control (AF-SCHED-01) | Should GPUs share the CPU and memory admission and enforcement model? | Agent workloads use local GPUs at a scale that contends | AD-0005 | exploratory |
| EX-04 | Placing whole agent sessions or long-running services on other nodes | Run an entire agent workspace where capacity is | Clients keep session state locally; there is no remote execution environment to move to | LAN placement (AF-LAN-02) | Can sessions move between machines without breaking client state? | Clients support remote execution environments | AD-0008 | exploratory |
| EX-05 | macOS node | Serve developers on macOS | Out of scope by decision; a third platform backend doubles platform work | Platform abstraction boundaries (AD-0002) | Is the demand worth a third backend? | A product-owner decision | AD-0002 | exploratory |
| EX-06 | iOS app | Mobile monitoring and control on iOS | Android comes first; a second mobile platform doubles the work | The Android app delivered (AF-AND-02) | Is the demand worth a second mobile platform? | A product-owner decision after the Android app's use is known | AD-0015 | exploratory |

## 4. Maintenance and promotion

- **One place.** Deferred work is recorded only here. Task records point to it (`out_of_scope: … (roadmap RM-xx)`), and the Design cites the same IDs. `python tools/plan.py validate --design <Design root>` checks that:
  - the IDs are unique and well formed (`RM-NN`, `EX-NN`; malformed IDs are reported, not skipped);
  - every field is filled and statuses are valid;
  - referenced tasks, requirements and decisions exist;
  - every `RM-*` or `EX-*` cited in the Design exists here.
- **Changes** are reviewed Plan PRs. A product decision that adds, changes or drops an item is recorded in the same PR that updates the row. Rows are never deleted: their status becomes `promoted: AF-…` or `dropped: <reason>`.
- **Revisiting.** At each milestone's end, the coordinator notes items whose *Revisit when* condition may hold in its report. It never starts them.
- **Promotion** turns an item into actionable work:
  1. The product owner decides, or confirms that the *Revisit when* condition holds.
  2. A Design PR adds or amends requirements, decisions, architecture, contracts and pages; it is independently reviewed and merged.
  3. A Plan PR adds tasks with scope, dependencies, acceptance criteria and verification to the delivery graph, sets the row's status to `promoted: <task IDs>`, and is independently reviewed and merged after the Design PR.
  4. Only then can the tasks be selected for execution ([execution-prompt.md](execution-prompt.md)).

  An exploratory idea becomes accepted future work (`accepted as RM-xx`) only through a recorded product-owner decision.
- **Foundations.** When a future item needs interfaces or data earlier, the foundation becomes part of a committed task, and the row's *Foundations in release 1* column names it. The feature itself stays here.
