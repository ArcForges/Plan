# Future scope — no current implementation

## 1. Accepted deferred interests

| ID | Item | Purpose | Why deferred | Prerequisites | Revisit when | Foundations in V2 | References | Status |
|---|---|---|---|---|---|---|---|---|
| RM-01 | Additional native platforms or CPU architectures | Broader reach | No current qualification or user delivery authorization | Stable official backend and full native evidence | Owner explicitly expands support | None beyond current concrete profile records | AD-0022 | accepted |
| RM-02 | Additional managed application types | Broader use cases | Current product is CLI only | Separate security/lifetime/UI requirements | Owner changes product boundary | None; no GUI client or interface shells | AD-0022 | accepted |

## 2. Exploratory topics

| ID | Idea | Purpose | Why not now | Prerequisites | Question to answer | Revisit when | References | Status |
|---|---|---|---|---|---|---|---|---|
| EX-01 | Plugins/network-management extensions | Potential future extensibility | Not needed for current product | Explicit owner research request | Does it solve a validated user need? | After current scope acceptance and new authorization | AD-0022 | exploratory |
| EX-02 | GPU or advanced resource dimensions | Potential specialized control | No current delivery requirement | Official support and distinct evidence | Is a portable enforceable contract possible? | Explicit new product decision | AD-0022 | exploratory |

## 3. Cancelled scope

AI/MCP/Hook integration, Task DAG/retries, toolchain/cache/CAS/worktree platforms, LAN distribution, mobile/desktop clients and GUI sandboxing have no active task or prerequisite. Historical ideas remain in the immutable archive. Ordinary in-sandbox caches require no feature.

## 4. Promotion

A roadmap row authorizes no code, abstract interface, table or dependency. Promotion needs an explicit owner direction, a reviewed Design change and a new detailed AFV2 task with real dependencies and verification. Deferred interests do not hold current acceptance open.
