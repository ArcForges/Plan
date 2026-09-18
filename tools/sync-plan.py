#!/usr/bin/env python3
"""Generate/check navigation against one clean, accepted Design checkout. Standard library only."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

PROJECTS = Path('C:/MyFile/Projects')
PLAN = PROJECTS / 'Plan'
DESIGN = PROJECTS / 'ArcForges-Design'
PROMPT = PROJECTS / 'arcforges-implementation-prompt.md'
EXCLUDED = {'20': 'future-only', '27': 'retired', '29': 'retired'}
WP_DIR = 'docs/planning/work-packages'
STEP_RE = re.compile(r'^### WP-(\d{2}\.\d{2}[A-Z]?)\s+[—–-]\s+(.+)$', re.M)
LINK_RE = re.compile(r'\]\(([^)\n]+)\)')

# Extra concrete authorities found by searching the whole corpus, beyond WP input tables.
# Short keys below are generator notation only; the rendered reading map uses real paths/titles.
SUPPLEMENTS = {
 '00': 'R00 R01 A00 A01 A27 provenance refs reconcile',
 '01': 'A00 A01 A19 A21 A27 reconcile',
 '02': 'A01 A14 A21 A22 A25 R12',
 '03': 'C00 C01 C02 C03 C04 C05 C06 C07 C08 C09 C10 C11 M00 M01 M02 M03 M04 M05 A26 A27 R07 R13 Notes Scope Slate',
 '04': 'C00 C04 A02 M00 R12',
 '05': 'A00 A01 A02 A21 A27 C04 C11 invariant traceability',
 '06': 'A03 A04 A05 A11 A12 A14 A21 A25 C04 C05 C09 C10 M04 R12 X03',
 '07': 'A06 A07 M00 M02 M03 M05 R13',
 '08': 'A03 A24 A27 C02 C09 M02',
 '09': 'A02 A04 A27 C00 C02 C08 C10 R08 R09',
 '10': 'A04 A27 R09 R12 X01 X03',
 '11': 'A08 A24 C00 C09 C11 R07 M00',
 '12': 'A13 R07 R12 X03',
 '13': 'A12 A18 A21 A23 A24 A26 A27 C06 C09 Notes Scope Slate scope-ref slate-ref provenance',
 '14': 'A04 A19 A27 C02 C07 C10 Notes X01 X03',
 '15': 'A27 M02 M03 M05 C07 C10 Chat X01 X03 chat-ref',
 '16': 'A09 A17 C00 C02 C03 C07 C10 M00 M01 M02 R05 X03',
 '17': 'A04 A09 A27 C07 C10 M05 Chat X01 X03 chat-ref',
 '18': 'A06 A18 A19 A26 C02 M02 M04 Notes notes-ref R13',
 '19': 'A06 A07 A18 A26 M02 M03 C07 R06 R13 Notes notes-ref',
 '21': 'A05 A22 C05 M00 M01 M04 Cloud R03',
 '22': 'A08 A10 C01 C04 C07 C10 C11 M01 M04 R02 R07 X03',
 '23': 'A02 A05 A25 C00 C01 C03 C04 C07 C10 C11 M04 R12 X03',
 '24': 'A05 C03 C05 C10 M01 M04 X03 R03',
 '25': 'A06 A07 A20 C01 C07 C10 M00 M01 M02 M04 M05 R03 R13 Notes X03',
 '26': 'A09 C02 C03 C07 C10 C11 M01 M02 M04 R05 X03',
 '28': 'A18 A26 C02 C07 M01 M02 M03 M04 Notes R13 notes-ref',
 '30': 'A11 C04 C07 C10 M05 Mobile X02 X03 chat-ref',
 '31': 'A11 C03 C07 C10 Mobile X02 X03 chat-ref',
 '32': 'A11 A14 A21 A22 C04 Mobile R10 R12 X02 X03 distribution-ref',
 '33': 'A12 A19 A21 A23 A26 C02 C06 M02 Scope scope-ref',
 '34': 'A19 A26 C02 M02 M03 Scope scope-ref',
 '35': 'A07 A23 A26 C02 C04 C06 M02 M04 R13 Scope scope-ref',
 '36': 'A06 A12 A19 A26 C02 C06 M02 Slate slate-ref',
 '37': 'A12 A21 A24 A26 C06 C09 M02 M03 Slate slate-ref',
 '38': 'A12 A21 A26 C06 M02 M03 Slate slate-ref',
 '39': 'A06 A07 A23 A26 C02 C06 C07 M02 M04 R13 Slate slate-ref',
 '40': 'A09 A17 C05 C07 C10 M01 M03 M04 M05 R06 Notes Chat',
 '41': 'A15 A24 C02 C08 C09 C11 M01 M02 R08 X03',
 '42': 'A16 A20 C01 C07 C08 M00 M01 M04 R04 figures',
 '43': 'A09 A16 A17 C05 C07 M00 M01 M04 R04 R05 figures',
 '44': 'A05 A16 A20 C08 C11 M01 M04 R11 X03',
 '45': 'A10 A13 A15 A25 C04 C07 C08 C11 M01 M04 R07 R10 Cloud Web X03',
 '46': 'A07 A20 A22 C05 C07 M00 M01 M02 M04 M05 R03 R13 Cloud X03',
 '47': 'A10 A14 A25 R09 R12 Web X03 distribution-ref',
 '48': 'A08 A10 A16 A20 A25 C01 C07 C10 M01 M04 R02 R04 Web X03',
 '49': 'A10 A25 A27 C03 C07 C10 M05 Mobile Web X01 X03',
 '50': 'A14 A21 A22 A25 C05 M04 R04 R10 R12 Cloud Web Mobile figures distribution-ref X03',
 '51': 'A05 A23 A26 C04 C06 M00 M01 M04 Scope R04',
 '52': 'A09 A17 A20 C03 C05 C07 C10 M00 M01 M03 M04 M05 R05 Chat X03',
 '53': 'A14 A21 A22 C04 C07 C08 R10 R12 distribution-ref X03',
}

FOCUS = {
 '00': 'Freeze current authority, names, rights and reusable policy evidence. No future package or Cloud manifest is an input; completed source/reference audits are consumed and checked for drift.',
 '01': 'Reconcile the nine actual repositories against their current HEADs. The ede43db monorepo inventory is historical disposition evidence, not a target tree to recreate.',
 '02': 'Own toolchain/build-policy and candidate pipelines. Preserve independent roots and staged producer availability; full functional native packages are WP13.',
 '03': 'Produce the complete initial NuGet/npm/Maven contract closure, all concrete operation metadata and independent semantic fixtures. Business handlers belong to later owners; contract completeness cannot be deferred to them.',
 '04': 'Implement exact value/error/version primitives without a future database dependency. Use the current producer registry for Foundation ownership and consumer adapters.',
 '05': 'Enforce current architecture and repository policy. A scoped invariant test/accounting contribution does not close every future implementation gate.',
 '06': 'Run actual minimal AOT, browser, Kotlin Android and Cloudflare transport/package proofs. Use the designated isolated probe ports; do not require the future full Harness.',
 '07': 'Produce persistence mechanisms with owner fixtures, exact atomicity/recovery and published package evidence. Product-specific schema behavior remains with product owners.',
 '08': 'Implement private parent/child helper gRPC only. In-process product ports, independent application sessions and future cross-product collaboration do not create local service listeners.',
 '09': 'Implement typed in-process contribution/capability/resource mechanisms over the published contracts, with final validation at the owning application.',
 '10': 'Deliver the reusable desktop shell/design system and applicable UI states. The embedded assistant is a package consumer within each application, not a fourth desktop executable.',
 '11': 'Implement security mechanisms and the real OS-restricted fixture-parser helper. Production parser composition is WP13.13, not a backwards prerequisite.',
 '12': 'Deliver reusable observability and explicit privacy/redaction evidence on this stage\'s actual hosts; later owner operations remain staged.',
 '13': 'Complete functional native/helper packages, dependencies and clean C17/C# AOT consumers. 13.05 proves all declarations/common layouts; 13.06–13.14 implement families; 13.15/13.90 verify complete packaged exports. 13.04 seeds inventory; 13.16 completes it.',
 '14': 'Compose an independent application using typed host ports and package-only mechanisms. Keep minimal ArcNotes owner behavior in ArcNotes.',
 '15': 'Produce isolated per-application assistant history/core packages and exact SQLite/history behavior. Export client fixtures are replaced by actual Cloud owners at WP25.08.',
 '16': 'Implement the device/product execution chain, command recovery and security. The sole Cloud model/tool loop remains WP52.',
 '17': 'Complete embedded assistant navigation, interactions and client mechanisms. Explicit future Cloud/automation/AI fixtures are allowed only until their named real producers, including WP52.06.',
 '18': 'Implement accepted Notes document/editor behavior, stable text/cell identity, IME, undo, containment and recovery; consume the existing reference matrix and original implementation boundaries.',
 '19': 'Implement local Notes search and portability. Distinguish local/client fixture acceptance from actual Cloud export production at WP25.08.',
 '21': 'Produce the real Container/Worker/D1 plan bridge, migration, receipts, fenced jobs and selfhost profile. Its integration manifest is progressive; future business owners remain pending.',
 '22': 'Produce real identity/session/browser-ceremony and mail paths with per-application isolation. Current P2-014 excludes sibling Device SSO. Later portal UI is not an authentication-producer prerequisite.',
 '23': 'Generate/register the complete public contract surface and prove real identity/transport behavior. Future owner fixtures are explicitly replaced at WP25/42/40/51/52; the Android WP06 probe suffices here.',
 '24': 'Produce bounded stream/hint delivery and durable cursor/unary recovery. Hints are not business authority; final Task/Harness content is integrated at WP52.',
 '25': 'Complete actual R2 lifecycle and Cloud Notes/Chat authority, history import/export, sync and conflicts. Client fixtures from WP15/19 are replaced here.',
 '26': 'Implement presence and a durable one-application device bridge with owner reauthorization, deduplication and unknown-effect reconciliation; real model-driven orchestration closes at WP52.',
 '28': 'Complete Notes typed properties, scalar queries and views using real Cloud owner behavior, preserving existing light scope and import/export fidelity.',
 '30': 'Produce Kotlin Android foundation, Room/security/OS adapters and package-only Maven clients against actual WP23–25. Task/AI fixtures are temporary until WP31/WP52.',
 '31': 'Complete the Android UI and companion flows against real Harness, Cloud and one-application bridge. Real push sender WP45.09 is already upstream.',
 '32': 'Verify signed Android distribution on actual required devices/channels, signing identity, consumption-only rules, push and non-GMS fallback. Missing external access remains a named gate.',
 '33': 'Implement real acquisition sources and durable capture/replay with source/framing/time/loss profiles. Synthetic data cannot close required hardware evidence.',
 '34': 'Implement Scope measurements, analyses, decoders, triggers and reports with independent numeric/gap vectors from the product behavior profiles.',
 '35': 'Complete Scope capability/context, metadata sync and portability. Raw capture upload stays explicit and bounded; real Cloud simulator integration is WP51.',
 '36': 'Implement Slate project/timeline/editing with exact time and recovery semantics, before playback/render consumers.',
 '37': 'Implement real native decode/playback, clocks, retime/effect/audio graphs and contained parsing; honor portable paths and optional backend distinctions.',
 '38': 'Complete colour, scopes, render/encoding/subtitle profiles and atomic export; verify declared numeric tolerances rather than inventing cross-encoder byte identity.',
 '39': 'Complete Slate packaging, relink, metadata sync and bidirectional OTIO fidelity. Real AI transcription/adoption integrates later at WP52.',
 '40': 'Produce actual application-scoped derived search/retrieval with current permissions, consent and citations. No cross-product aggregator is introduced.',
 '41': 'Produce extension host/protocol, package/connector lifecycle, public SDK/CLI and actual PackageCatalog APIs. WP45.10 consumes these APIs for review/revocation UI.',
 '42': 'Implement technical commerce and test-mode proof. Execute 42.11 before 42.10. Actual receipt, payout, pricing activation and customer journey remain gated at WP48/50.',
 '43': 'Implement actual Workers AI routing/metering and uncertain-outcome handling. Execute 43.07 before 43.06; recorded fixtures complement real supplier/usage evidence.',
 '44': 'Produce typed policy/configuration authority with deterministic rollout, history and last-known-good recovery before its AI/search/operations consumers.',
 '45': 'Build actual Operations UI, customer push sender and PackageCatalog review. Rehearse implemented paths now; backup/Harness/combined disaster evidence joins at WP46/52/50.',
 '46': 'Prove independent D1/R2 backup and fresh restore, generation fencing and denial of old effects/credentials. Combined active Harness recovery still closes at WP50.',
 '47': 'Produce Web tooling/design system and static site before WP45. Approved-shape test offers/downloads are fixtures; real public projection and activation close at WP50.',
 '48': 'Deliver real account/session/commerce/export UI using the actual upstream producers; activation still requires the applicable real provider evidence.',
 '49': 'Complete browser Chat UI against actual Cloud/Harness/device bridge. Apply browser session/CSP/fallback policy rather than Android-only or local-desktop behaviors.',
 '50': 'Join all required real product, platform, provider, store, operational and commercial evidence. Promote the same tested immutable bytes; no required fixture-backed route may pass as release.',
 '51': 'Implement real deterministic simulator jobs, fenced D1 segment/checkpoint publication and R2 delivery into Scope. Synthetic results remain labelled and cannot prove hardware.',
 '52': 'Implement the sole Workflow Harness with actual model/usage, local/Cloud/temporary modes, same-application tools and automation. Replace assigned earlier client fixtures and preserve uncertain effects.',
 '53': 'Produce the updater and distribution trust with real staged apply/rollback. Keep the source numbering gap: 53.06 does not exist. Test signing proves mechanics; WP50 verifies production release trust.',
}

COMMON = [
 'AGENTS.md', 'README.md', 'docs/decisions/README.md',
 'docs/decisions/phase-1-foundation-decisions.md', 'docs/decisions/phase-2-specification-decisions.md',
 'docs/planning/README.md', 'docs/planning/implementation-sequence.md',
 'docs/planning/work-packages/README.md', 'docs/planning/producer-artifacts-and-integration.md',
 'docs/requirements/README.md', 'docs/architecture/README.md',
 'docs/assurance/invariant-coverage.md', 'docs/assurance/traceability-matrix.md',
 'docs/assurance/testing-and-verification-strategy.md', 'docs/assurance/open-gates-register.md',
 'docs/assurance/release-gates.md',
]
HISTORY_NAMES = {
 'phase-1-official-verification.md', 'phase-1-input-review-ledger.md',
 'evidence-driven-revisions.md', 'implementation-state-reconciliation.md',
}


def git(*args: str) -> str:
    return subprocess.check_output(['git', '-C', str(DESIGN), *args], text=True, encoding='utf-8').strip()


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def plain(text: str) -> str:
    return re.sub(r'[`*]', '', text).strip()


def link(label: str, path: Path, anchor: str = '') -> str:
    return f'[{label}](<{path.as_posix()}{"#"+anchor if anchor else ""}>)'


def title(text: str, fallback: str) -> str:
    m = re.search(r'^# (.+)$', text, re.M)
    return plain(m[1]) if m else fallback


def local_refs(rel: str, text: str) -> list[str]:
    result = set()
    for raw in LINK_RE.findall(text):
        raw = raw.strip('<>')
        raw = unquote(raw.split('#')[0])
        if not raw or ':' in raw:
            continue
        path = (DESIGN / rel).parent.joinpath(raw).resolve()
        assert path.is_relative_to(DESIGN.resolve()), (rel, raw)
        assert path.exists(), ('missing cited path', rel, raw)
        if path.is_file() and path.suffix == '.md':
            result.add(path.relative_to(DESIGN.resolve()).as_posix())
    return sorted(result)


def load():
    assert not git('status', '--porcelain'), 'Use a clean Design checkout at the accepted commit.'
    head = git('rev-parse', 'HEAD')
    paths = git('ls-files', '*.md').splitlines()
    docs = {p: (DESIGN / p).read_text('utf-8') for p in paths
            if not (p.startswith('docs/deprecated-inputs/') and p.endswith('-deprecated.md'))}
    seq = docs['docs/planning/implementation-sequence.md']
    order_match = re.search(r'^Serial execution: ([\d, ]+)\.', seq, re.M)
    assert order_match, 'Missing explicit serial order'
    order = order_match[1].split(', ')
    assert len(order) == len(set(order))
    assert not set(order) & EXCLUDED.keys()
    graph_text = seq[seq.index('## 9.'):order_match.start()]
    graph = {}
    for n, body in re.findall(r'^\| (\d{2}) \| (.*?) \|$', graph_text, re.M):
        graph[n] = re.findall(r'`(\d{2})`', body)
    assert set(graph) == set(order), 'Graph/order differ'
    positions = {n: i for i, n in enumerate(order)}
    for n, parents in graph.items():
        assert len(parents) == len(set(parents))
        assert all(positions[p] < positions[n] for p in parents), ('dependency inversion', n, parents)
    aliases = {}
    for prefix, folder in [('R', 'requirements'), ('A', 'architecture'), ('C', 'architecture/contracts'),
                            ('M', 'architecture/data-model'), ('X', 'experience')]:
        for p in docs:
            if Path(p).parent.as_posix() == 'docs/' + folder and re.match(r'\d{2}-', Path(p).name):
                aliases[prefix+Path(p).name[:2]] = p
    aliases.update({
        'Notes': 'docs/requirements/products/arcnotes.md', 'Scope': 'docs/requirements/products/arcscope.md',
        'Slate': 'docs/requirements/products/arcslate.md', 'Chat': 'docs/requirements/products/arcchat.md',
        'Mobile': 'docs/requirements/products/arcchat-mobile-and-web.md',
        'Cloud': 'docs/requirements/products/arcforges-cloud.md', 'Web': 'docs/requirements/products/arcforges-web.md',
        'provenance': 'docs/assurance/reference-coverage-and-provenance.md',
        'refs': 'docs/assurance/reference-coverage/README.md',
        'reconcile': 'docs/assurance/implementation-state-reconciliation.md',
        'invariant': 'docs/assurance/invariant-coverage.md', 'traceability': 'docs/assurance/traceability-matrix.md',
        'figures': 'docs/assurance/commercial-figure-status.md',
        'chat-ref': 'docs/assurance/reference-coverage/arcchat-aionui.md',
        'notes-ref': 'docs/assurance/reference-coverage/arcnotes-affine-siyuan.md',
        'scope-ref': 'docs/assurance/reference-coverage/arcscope-serial-studio.md',
        'slate-ref': 'docs/assurance/reference-coverage/arcslate-arcvideo.md',
        'distribution-ref': 'docs/assurance/reference-coverage/distribution-startarcforges.md',
    })
    wps = {}
    for rel, text in docs.items():
        name = Path(rel).name
        if Path(rel).parent.as_posix() != WP_DIR or not re.match(r'\d{2}-', name):
            continue
        n = name[:2]
        if n in EXCLUDED:
            continue
        assert n in order
        clean = re.sub(r'<a\b[^>]*>\s*</a>', '', text)
        steps = [(m[1], m[2].strip()) for m in STEP_RE.finditer(clean)]
        all_owning_headers = re.findall(r'^#{1,6} WP-(\d{2}\.\d{2}[A-Z]?)(?![\d.A-Z])', clean, re.M)
        assert all_owning_headers == [s for s, _ in steps], ('unsupported owning heading shape', rel)
        assert steps and all(s.startswith(n+'.') for s, _ in steps)
        assert len({s for s, _ in steps}) == len(steps)
        assert steps[-1][0] == n+'.90'
        assert all(f'id="rule-wp-{s}"' in text for s, _ in steps)
        for nested in re.findall(r'^#{3,6} WP-(\d{2}\.\d{2}[A-Z]?\.\d+(?:\.\d+)*)\b', clean, re.M):
            assert '.'.join(nested.split('.')[:2]) in {s for s, _ in steps}, ('orphan nested section', nested)
        assert set(re.findall(r'`(\d{2})`', re.search(r'^> Upstream:(.+?)· Downstream:', text, re.M)[1])) == set(graph[n])
        wps[n] = {'path': rel, 'title': title(text, name), 'steps': steps,
                  'direct': local_refs(rel, text), 'extra': [aliases[k] for k in SUPPLEMENTS[n].split()]}
    assert set(wps) == set(order) == set(SUPPLEMENTS) == set(FOCUS)
    for n in order:
        assert set(wps[n]['extra']).issubset(docs)
    return head, docs, order, graph, wps


def historical(path: str) -> bool:
    return Path(path).name in HISTORY_NAMES or ('/assurance/' in path and any(x in Path(path).name for x in ['review', 'verification', 'repair'])) and Path(path).name != 'testing-and-verification-strategy.md'


def render_list(head, docs, order, graph, wps):
    flat = [(n, ident, name) for n in order for ident, name in wps[n]['steps']]
    lines = [
        '# ArcForges implementation sequence', '',
        f'Design baseline: `{head}`. {len(order)} active work packages, {len(flat)} owning substeps, {sum(map(len, graph.values()))} dependency edges.', '',
        'Copy **one code block** below into a fresh or continuing AI task. Each block names the reusable prompt, the exact formal owning section and its reading context. No substitution or whole-WP selection is needed. Start at 00.00; select the next entry yourself after checking the current receipt.', '',
        'This is an execution index, not a second specification or a progress ledger. A listed/compiled document is not an accepted implementation. Read the prompt and the [reading map](reading-map.md); check the [execution receipts](execution/README.md). Each run must freshly search current related Design beyond these entry points.', '',
        'Order follows implementation-sequence §9, then owning headings in each WP. Explicit source ordering preserves 42.11 before 42.10 and 43.07 before 43.06. Each .90 is a separate final stage gate. WP20 is future-only; WP27/29 are retired; no missing numeric ID is synthesized. Nested NN.MM.K sections stay with their owning NN.MM[A].', '',
        'Prerequisites are the direct upstream WPs and preceding substeps within the current WP, at their prescribed stages. The navigation sequence does not add prerequisite edges. Future evidence is pending only where the formal producer matrix explicitly permits it.', '',
        '## Work-package navigation', '', '| Position | Work package | Substeps | Direct upstream WPs |', '|---|---|---:|---|',
    ]
    for i,n in enumerate(order,1):
        label=wps[n]['title'].replace('|','\\|')
        lines.append(f'| {i} | [{label}](#wp-{n}) | {len(wps[n]["steps"])} | {", ".join(graph[n]) or "None"} |')
    lines += ['', '## Copy one substep', '']
    index = 0
    for n in order:
        w=wps[n]
        lines += [f'<a id="wp-{n}"></a>', f'### {wps[n]["title"]}', '',
                  f'Full WP: {link("formal source", DESIGN / w["path"])}. Reading context: [WP{n}](reading-map.md#wp-{n}).', '',
                  f'Direct upstream WPs: {", ".join(graph[n]) or "none"}. {FOCUS[n]}', '']
        for ident,name in w['steps']:
            index += 1
            anchor = ident.lower().replace('.', '-')
            lines += [f'<a id="substep-{anchor}"></a>', f'#### {index:03d}. {ident} — {name}', '', '```text',
                f'Read and follow {PROMPT}.',
                f'Execute only ArcForges Substep {ident} — {name}.',
                f'Owning document: {DESIGN / w["path"]}',
                f'Owning section: WP-{ident}; explicit anchor: rule-wp-{ident}.',
                f'Read the common context and WP{n} entry in {PLAN / "reading-map.md"} (anchor wp-{n}); then freshly search all related current Design beyond those entry points.',
                'Include this substep\'s nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.',
                '```', '']
    lines += ['End of the active sequence. Acceptance of 50.90 requires the real joined evidence defined by Design; the existence of this list closes no product gate.', '']
    return '\n'.join(lines)


def render_map(head, docs, order, graph, wps):
    lines = ['# ArcForges reading map', '', f'Design baseline: `{head}`.', '',
        'This map is navigation, not exhaustive authority. It combines file citations from **the entire body of every active WP**, including late amendments and .90, with concrete authorities found by searching the current corpus. For a selected substep, read its whole WP, then the applicable definitions and tests in these files. Follow section anchors and rule IDs in the original WP; freshly search incoming references and other relevant files too.', '',
        'A cited later WP or an early reference to a release gate is context, not an additional dependency. The formal graph and producer stage matrix decide which input must exist now. Dated reviews and bound historical inventories explain earlier findings; use their current formal owners for behavior.', '',
        '## Common context', '',
        'Read the execution instructions, accepted decisions and planning entry points. Consult the applicable rows of the invariant, traceability, testing and release-gate authorities; do not treat every future release gate as a prerequisite of the current substep.', '',
    ]
    for p in COMMON:
        assert p in docs
        lines.append('- '+link(p,DESIGN/p))
    lines += ['', '## Reference sources and exclusions', '',
        'All reference roots below exist at preparation time and remain read-only. Start with the completed coverage matrix; inspect the relevant source/commit only for this task or drift. A path in an older matrix may use the former root: resolve the actual repository identity at the path below. Do not infer permission to copy from availability or an AI rewrite.', '',
        '| Area | Actual root(s) | Coverage authority |', '|---|---|---|',
        f'| Assistant and Android UX | `C:\\MyFile\\Projects\\AionUi` (including `mobile`) | {link("AionUi matrix",DESIGN/"docs/assurance/reference-coverage/arcchat-aionui.md")} |',
        f'| Notes | `C:\\MyFile\\Projects\\AFFiNE`; `C:\\MyFile\\Projects\\siyuan` | {link("Notes matrix",DESIGN/"docs/assurance/reference-coverage/arcnotes-affine-siyuan.md")} |',
        f'| Scope | `C:\\MyFile\\Projects\\Serial-Studio` | {link("Scope matrix",DESIGN/"docs/assurance/reference-coverage/arcscope-serial-studio.md")} |',
        f'| Slate | `C:\\MyFile\\Projects\\ArcVideo`; `C:\\MyFile\\Projects\\ArcVideoFoundation` | {link("Slate matrix",DESIGN/"docs/assurance/reference-coverage/arcslate-arcvideo.md")} |',
        f'| Distribution shape/notices only | `C:\\MyFile\\Projects\\StartArcForges` | {link("packaged-output boundary",DESIGN/"docs/assurance/reference-coverage/distribution-startarcforges.md")} |', '',
        'Observe per-file provenance and excluded/proprietary subtrees. Reference capability does not create product scope. Do not execute, unpack, disassemble or reverse engineer StartArcForges binaries. Deprecated input bodies are excluded; historical citations do not reopen them. The old monorepo is not the current implementation root.', '',
        '## Current authority catalogue', '',
        'These are available search surfaces, not a demand to read the whole corpus for every substep. The package-specific maps below narrow the initial reading. Current amendments govern historically named files.', '',
    ]
    for folder in ['docs/requirements', 'docs/architecture', 'docs/experience']:
        lines += [f'### {folder}', '']
        for p in sorted(docs):
            if p.startswith(folder+'/'):
                lines.append('- '+link(p,DESIGN/p)+' — '+title(docs[p],Path(p).name))
        lines.append('')
    lines += ['## Work-package reading contexts', '']
    for n in order:
        w=wps[n]
        direct=set(w['direct']); extra=set(w['extra'])
        refs=sorted((direct|extra)-set(COMMON))
        refs=[p for p in refs if not p.startswith(WP_DIR+'/')]
        norm=[p for p in refs if not historical(p)]
        history=[p for p in refs if historical(p)]
        lines += [f'<a id="wp-{n}"></a>', f'### {w["title"]}', '',
            f'Parent: {link(w["path"],DESIGN/w["path"])}. Read the **whole file**, including governing prose outside the selected numbered section.', '',
            f'Direct upstream WPs: {", ".join(graph[n]) or "none"}. Within this WP, use source heading order shown in [list.md](list.md#wp-{n}) and verify earlier substep receipts; preserve the declared stage.', '',
            FOCUS[n], '',
            'Search leads: '+ '; '.join(name for ident,name in w['steps'] if not ident.endswith('.90'))+'.', '',
            'Concrete authorities and verification inputs (in addition to common context):', '',
        ]
        for p in norm:
            assert p in docs, p
            origin='WP citation' if p in direct else 'additional current authority'
            lines.append('- '+link(p,DESIGN/p)+f' — {origin}.')
        if history:
            lines += ['', 'Bound inventory / historical evidence; follow current normative owners when amended:', '']
            for p in history:
                lines.append('- '+link(p,DESIGN/p))
        lines.append('')
    return '\n'.join(lines)


def check_generated(listing, mapping, docs, order, graph, wps):
    flat=[(n,i,t) for n in order for i,t in wps[n]['steps']]
    blocks=re.findall(r'```text\n(.*?)\n```',listing,re.S)
    assert len(blocks)==len(flat)
    ids=[]
    for block,(n,ident,name) in zip(blocks,flat):
        assert f'Execute only ArcForges Substep {ident} — {name}.' in block
        assert f'Owning document: {DESIGN / wps[n]["path"]}' in block
        assert f'explicit anchor: rule-wp-{ident}.' in block
        assert str(PROMPT) in block and str(PLAN/'reading-map.md') in block
        ids.append(ident)
    assert len(ids)==len(set(ids))
    assert ids.index('42.11') < ids.index('42.10')
    assert ids.index('43.07') < ids.index('43.06')
    assert ids[-1]=='50.90' and ids[0]=='00.00' and '53.06' not in ids
    assert len(re.findall(r'<a id="substep-',listing))==len(flat)
    # All generated link targets must exist; explicit generated fragments must resolve.
    for text in [listing,mapping]:
        for target in LINK_RE.findall(text):
            raw=target.strip('<>'); path,_,fragment=raw.partition('#')
            if not path: continue
            p=Path(path) if re.match(r'^[A-Za-z]:/',path) else PLAN/path
            if p.name in ['list.md','reading-map.md']:
                contents=listing if p.name=='list.md' else mapping
                assert not fragment or f'id="{fragment}"' in contents
            else:
                assert p.exists(),('bad output link',target)
    # Coverage: no active requirements/architecture/experience file is absent from the catalogue.
    for p in docs:
        if p.startswith(('docs/requirements/','docs/architecture/','docs/experience/')):
            assert (DESIGN/p).as_posix() in mapping
    return len(flat)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--write', action='store_true', help='Regenerate indexes after reviewing the accepted Design and curated map.')
    group.add_argument('--check', action='store_true', help='Read-only verification; fail on document/prompt/navigation drift.')
    args=parser.parse_args()
    head,docs,order,graph,wps=load()
    listing=render_list(head,docs,order,graph,wps)
    mapping=render_map(head,docs,order,graph,wps)
    total=check_generated(listing,mapping,docs,order,graph,wps)
    outputs={'list.md':listing,'reading-map.md':mapping}
    snapshot={
        'design_root':str(DESIGN), 'design_commit':head,
        'work_packages':len(order), 'substeps':total, 'dependency_edges':sum(map(len,graph.values())),
        'serial_order':order, 'excluded':EXCLUDED,
        'prompt_path':str(PROMPT),'prompt_sha256':digest(PROMPT.read_bytes()),
        'generated_sha256':{k:digest(v.encode('utf-8')) for k,v in outputs.items()},
        'source_sha256':{p:digest(t.encode('utf-8')) for p,t in sorted(docs.items())},
    }
    outputs['baseline.json']=json.dumps(snapshot,indent=2,ensure_ascii=False)+'\n'
    if args.write:
        for name,value in outputs.items():
            (PLAN/name).write_text(value,encoding='utf-8',newline='\n')
    else:
        for name,value in outputs.items():
            assert (PLAN/name).read_text('utf-8')==value, f'{name} drifted; review changes before --write.'
    print(json.dumps({'mode':'write' if args.write else 'check','design':head,'documents_scanned':len(docs),
        'work_packages':len(order),'substeps':total,'dependency_edges':sum(map(len,graph.values())),
        'copy_blocks':total,'result':'PASS'},indent=2))

if __name__=='__main__':
    try:
        main()
    except (AssertionError,KeyError,ValueError) as exc:
        print('FAIL:',str(exc),file=sys.stderr)
        sys.exit(1)
