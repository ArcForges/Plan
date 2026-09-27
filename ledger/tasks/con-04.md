---
task: CON.04
status: complete
recorded: 2026-09-28
claimant: w-20260927-dother
epoch: 1
---

# Content sandbox contract surface

- Implementation: [Contracts PR54](https://github.com/ArcForges/Contracts/pull/54). Reviewed head `558fe782daeb361ee0701da867e1804fc7360125`; independent review [5860594404](https://github.com/ArcForges/Contracts/pull/54#issuecomment-5860594404); merge/source `018cd3493b30c7259da8ba42f8f2618e6a84afef`. Integrator confirmed clean primary fast-forward.
- Outcome: all 15 ContentSandboxService methods have exact three-message envelopes and 12 new bounded records, preserving SandboxLimits. Generated service descriptors supply parent/child direction and permitted role lookup. The existing internal Sandbox package references the already admitted Foundation producer and centrally pinned Grpc.Core.Api, with no new package identity or dependency version.
- Shape boundary: bounded image, PDF, tile and text projections; valid UTF-16 scalar pairs; at most 1024 text boxes and 64 KiB complete ExtractPdfText response; tile geometry, sequence and granted capacity; 2048 tile and 64 MiB limits. Padded final row length is bounded between `(height-1)*stride+rowBytes` and `height*stride` within the granted capacity.
- Source ownership: task constraint shard is combined by the actually delivered CON01 loader. Full official generation is clean. Fifteen operation exports retain the exact helper-parent/private-helper authorization profile from annex09. Access, provenance and dependency successors preserve accepted immutable history.
- Independent tests: typed ContentSandbox request/response fixtures test descriptors, roles, bounded geometry and malformed values without reflection-based protobuf JSON construction. Retained StructureTests also passed 86 independent shape fixtures, 353 Foundation cases and 199 extension/policy cases. Retained Native AOT serialization passed with the Sandbox catalogue preserving descriptor/cardinality assertions. Offline runtime validators do not grant resources or execute untrusted media.
- Narrow scanner support: Design87 merged d797e7836b86a6bb3be4d7d27c9de4a33271e5cd and Plan55 merged 7b458cba37230a8507d6961398c5e3a68fdadcc1 authorize only actually observed public input-hash false positives in two exact task-owned JSON paths. Every exception keeps exact rule/path/key/hash/whole-line matching and negative regression coverage, with immutable source snapshot proof.
- Limits: no OS helper launch, parent provisioning, resource-grant enforcement, digest/private-copy implementation, hostile-media parsing, installed-consumer behavior or production deployment is claimed. Those remain the corresponding runtime implementation owners' responsibilities.

- Final support checks: access inventory 190 types/435 files; provenance 944 files/106 records; dependency admission 145 dependencies/190 inputs; 21 admission regression tests and full formatting passed.
- Original source publication: [run 36357254970](https://github.com/ArcForges/Contracts/actions/runs/36357254970), candidate `1.0.0-ci.213.1`: Build candidate, Verify, Publish NuGet, Publish Maven channel and Publish npm all succeeded. [Security 36357255064](https://github.com/ArcForges/Contracts/actions/runs/36357255064) succeeded. Post-publication evidence is original job/commit status and primary fast-forward only.
