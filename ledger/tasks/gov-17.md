---
task: GOV.17
status: complete
recorded: 2026-09-27
claimant: w-20260927-ai-lane
epoch: 1
---

# Native retirement and retained image identity

## Outcome and obligation coverage

P2-019 native-family retirement and P2-020 ADP-10 source cleanup are satisfied. Media, Colour and Otio managed/runtime projects, ABI directories, OTIO overlay, package/solution/test registrations and the macOS Metal probe are removed. The native build retains only shim-static Image. The image directory is native/arcimage-abi and the owned logical library is ArcImageNative; the public header bytes and arc_image_* export set are unchanged from frozen DesktopPlatform e5ce94221c13d0014781a760c0865b942350be4d. The unchanged public header Git blob is d54944302778e76ec01ed6b50f441d295be0fed7. Internal source/header/test filenames remain compatible and do not create product ownership.

The package catalogue admits Build.Policy, Native.Abstractions, Native.Image and Native.Image.Runtime.win-x64 only. Packaging/RID/integrity guards and local consumer fixtures select Image. Existing historical published versions remain immutable and are not deleted or republished. New production runs do not publish retired packages.

Native profile r4 retains the exact previously reviewed 21 Image component source, licence, recipe and tool identities, with 21 superseding artifact records. All earlier profiles and source records remain unchanged. Explicit P2-019/GOV.17 retirement receipts allow only the exact former Media/Colour/Otio project/package/material registrations, reject missing historical evidence, active packages/projects and retained Image removal, and preserve the normal successor-chain requirement. The checker modifications are covered by contracts-provenance-tools-r2 under the original Apache licence.

## Review, integration and publication

Combined source PR: https://github.com/ArcForges/DesktopPlatform/pull/66. Final independently reviewed source head c5c6ec2ecd228e7d93b06067dc2ddc4c575d2e15; web_lane approval https://github.com/ArcForges/DesktopPlatform/pull/66#issuecomment-5858874475. Merged as 111a935e98a6666ec1dd965b095bcb8b95d9b80a after all 12 exact-head PR checks passed in https://github.com/ArcForges/DesktopPlatform/actions/runs/36343226842. Original main publication https://github.com/ArcForges/DesktopPlatform/actions/runs/36343608089 (run 28, attempt 1) succeeded, including publisher job 108692477350. The four retained NuGet packages ArcForges.Build.Policy, ArcForges.Native.Abstractions, ArcForges.Native.Image and ArcForges.Native.Image.Runtime.win-x64 were published at 1.0.0-ci.28.1. Original candidate nuget-candidate-36343608089-1 is GitHub artifact 10940272716, digest sha256:894cd878a70f6851b878e0982973a69835c7522aaf2966c09611ac9959a7bb23; its manifest retains individual package hashes. Successful publisher logs are the registry transfer receipt. No public package was downloaded again. Supporting root-solution scope repairs merged as Design77 at 2f274781fcd5414c42eff526a1aed8fcc1ece318 and Plan37 at 2a1449686c3c9a187a5706b6607b47faaf865a10; these supporting reviews do not constitute final product approval.

## Validation and limits

- Source provenance check passed against frozen e5ce94221c13d0014781a760c0865b942350be4d, preserving all immutable historical records; source and native profile consistency checked.
- 26 offline provenance tests and 21 native-closure tests passed, including exact retirement negatives and retained artifact disappearance rejection. Packaging fixtures now cover Image, missing CRT dependency, changed native bytes, required notices and RID mismatch.
- Local Image native C++ build produced ArcImageNative.dll; explicit opt-in ABI CTest passed 1/1. Existing Windows MSVC 14.51.36231 (compiler19.51.36257.0), Windows SDK10.0.28000.0, CMake4.4.3, Ninja1.13.2 and C:/vcpkg installed dependencies were used. This is local compatibility evidence, not the pinned production toolchain attestation. No toolchain was installed.
- Initial combined native CI successfully installed dependencies but failed managed restore with MSB3202 because root DesktopPlatform.slnx retained six removed Media/Colour/Otio project entries. Commit 93dae236a9840a71bcb43c48ffb3e8426eb9ee6b removes those six entries; all 37 project paths across both solutions exist. RID guard target identity also uses the stable arc_image prefix to avoid a non-admitted concatenated naming token. A subsequent managed CI exposed an obsolete expected count of 12 native bindings. Source fix b6baf50 (integrated in c5c6ec2) now asserts the exact three retained Image export identities, preserving owner-directory, duplicate, unknown-library and declaration checks. Final PR CI36343226842 and original main CI36343608089 passed native build, managed compilation/packaging and all policy checks.
- Native CI passed on the pinned production toolchain. A local managed test attempt found only SDK10.0.401 while global.json requires10.0.400; no toolchain or pin was changed, and official CI10.0.400 supplied the successful managed evidence. No downloaded published artifact, installed NuGet consumer, GUI, device, live-service or macOS execution is claimed. Native runtime tests remain local opt-in only. NAT.11 and NAT.30 retain real image capability and retained producer acceptance work; retirement does not certify product behavior.
- No completion prerequisites remain; no temporary runtime substitute introduced.
