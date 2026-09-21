# Repository guidance

- This repository owns execution profiles and task lists; formal documentation is English.
- Work in retained Git worktrees; append to related open PRs and leave unrelated PRs alone.
- Keep local/remote Current task and execution rules synchronized. Do not advance the task list without authorization.
- Follow [execution-policy.md](execution-policy.md) and Design P2-017. Never prescribe macOS CI, hosted runtime/device/browser/live-service/inference/installed-consumer tests or routine public-download/hash/install revalidation.
- Preserve necessary Windows/Linux build/offline/static/security and signing/licence/lock checks. Runtime checks are scoped local opt-in using existing tools, once per relevant change; no toolchain reinstall.
- Independent repository agents are allowed. Serialize heavy local builds and avoid hidden Git-hook builds.
- No explicit proxy or wsl.exe wrapper. Stop and identify a failed network operation instead of retrying or changing network settings.
- Review every PR and merge after applicable retained CI succeeds, or after review for docs-only PRs without CI. Post-merge: commit/job status and primary fast-forward only. Keep branches/worktrees and stop at the requested boundary.
