"""Offline tests for the delivery tool's coordination behavior.

Every remote is a local bare repository, so claim contention, compare-and-swap, takeover and the
authoritative-state rules run without the network. The graph is copied from the Design checkout
the tool would use ($ARCFORGES_DESIGN or the sibling of the Plan primary checkout).

    python -m unittest discover -s tools/tests -v
"""
import contextlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
from datetime import timedelta
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import delivery as d  # noqa: E402

DESIGN_SOURCE = d.default_design()


def sh(cwd, *args):
    r = subprocess.run(['git', '-C', str(cwd), *args], capture_output=True, text=True)
    if r.returncode:
        raise AssertionError(f'git {" ".join(args)}: {r.stderr}')
    return r.stdout.strip()


def ledger_text(task, status):
    return f'---\ntask: {task}\nstatus: {status}\nrecorded: 2026-09-25\nclaimant: test\n---\n\n## Evidence\n- test\n'


class Fixture:
    """Design and Plan bare remotes, a working clone of each and a second Plan clone (another worker)."""

    def __init__(self, root: Path):
        self.root = root
        self.design, self.plan, self.plan2 = root / 'design', root / 'plan', root / 'plan2'
        for name in ('design', 'plan'):
            sh(root, 'init', '--quiet', '--bare', str(root / f'{name}.git'))
            sh(root, 'clone', '--quiet', str(root / f'{name}.git'), str(root / name))
            sh(root / name, 'config', 'user.name', 'test')
            sh(root / name, 'config', 'user.email', 'test@example.invalid')
            sh(root / name, 'checkout', '--quiet', '-b', 'main')
        shutil.copytree(DESIGN_SOURCE / 'docs' / 'planning', self.design / 'docs' / 'planning')
        # The decision record that outOfScope markers name (DLV-43). Its own file, so use_full_design, which copies
        # the Design docs, cannot overwrite it while the P2-026 record is still unmerged on Design main.
        (self.design / 'docs' / 'decisions').mkdir(parents=True)
        (self.design / 'docs' / 'decisions' / 'scope-record-fixture.md').write_text(
            '# Scope decision record (fixture)\n\n<a id="rule-p2-026"></a>\n', encoding='utf-8')
        self.commit(self.design, 'design')
        (self.plan / 'ledger' / 'tasks').mkdir(parents=True)
        (self.plan / 'ledger' / 'README.md').write_text('# ledger\n', encoding='utf-8')
        self.commit(self.plan, 'plan')
        sh(root, 'clone', '--quiet', str(root / 'plan.git'), str(self.plan2))
        sh(self.plan2, 'config', 'user.name', 'test2')
        sh(self.plan2, 'config', 'user.email', 'test2@example.invalid')

    def commit(self, repo, message):
        sh(repo, 'add', '-A')
        sh(repo, 'commit', '--quiet', '-m', message)
        sh(repo, 'push', '--quiet', 'origin', 'HEAD:main')

    def record(self, task, status):
        (self.plan / 'ledger' / 'tasks' / f'{d.key_of(task)}.md').write_text(ledger_text(task, status), encoding='utf-8')

    def run(self, *argv, plan=None):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = d.main([*argv[:1], '--design', str(self.design), '--plan', str(plan or self.plan), *argv[1:]])
        return code, out.getvalue()

    def raw_claim(self, task, data, parent=None):
        return d.push_record(self.plan, 'claims', d.key_of(task), data, parent, 'test record')

    def claim_data(self, task, claimant='ghost', epoch=1, state='claimed', lease_hours=24.0, age_hours=0.0):
        now = d.utcnow() - timedelta(hours=age_hours)
        return {'schema': 1, 'kind': 'task', 'id': task, 'claimant': claimant, 'epoch': epoch, 'state': state,
                'claimedAt': d.iso(now), 'updatedAt': d.iso(now),
                'leaseUntil': d.iso(now + timedelta(hours=lease_hours)) if state in d.LIVE else None,
                'handoff': {'repository': 'Plan', 'branch': f'task/{d.key_of(task)}', 'prs': [], 'next': ['continue']}}


class DeliveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not (DESIGN_SOURCE / d.GRAPH_REL).is_file():
            raise unittest.SkipTest(f'no Design checkout at {DESIGN_SOURCE}')

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix='delivery-test-')
        self.fx = Fixture(Path(self.tmp))

    def tearDown(self):
        def unlock(func, path, _):  # Git marks object files read-only on Windows
            os.chmod(path, 0o700)
            func(path)
        shutil.rmtree(self.tmp, onexc=unlock) if sys.version_info >= (3, 12) else shutil.rmtree(self.tmp, onerror=unlock)

    # ---- readiness fails closed (finding 5) --------------------------------------------------

    def test_ready_lists_the_baseline_ready_set(self):
        code, out = self.fx.run('ready')
        self.assertEqual(code, 0, out)
        self.assertIn('Ready to start (1):', out)
        self.assertIn('ADOPT.01\tPlan', out)

    def test_ready_refuses_an_invalid_graph(self):
        p = self.fx.design / d.GRAPH_REL
        graph = json.loads(p.read_text(encoding='utf-8'))
        graph['tasks'][0]['lane'] = 'no-such-lane'
        p.write_text(json.dumps(graph, indent=1), encoding='utf-8')
        self.fx.commit(self.fx.design, 'break the graph')
        code, out = self.fx.run('ready')
        self.assertEqual(code, 1, out)
        self.assertIn('unknown lane', out)
        self.assertNotIn('Ready to start', out)

    def test_ready_refuses_an_invalid_ledger(self):
        self.fx.record('ADOPT.01', 'compelte')
        (self.fx.plan / 'ledger' / 'tasks' / 'GOV.04.md').write_text(ledger_text('GOV.04', 'delivered'), encoding='utf-8')
        self.fx.commit(self.fx.plan, 'bad ledger')
        code, out = self.fx.run('ready')
        self.assertEqual(code, 1, out)
        self.assertIn("unknown status 'compelte'", out)
        self.assertIn('must be named gov-04.md', out)

    def test_unknown_state_and_naive_timestamp_keep_the_task_unavailable(self):
        self.fx.raw_claim('ADOPT.01', dict(self.fx.claim_data('ADOPT.01'), state='claimd'))
        code, out = self.fx.run('ready')
        self.assertEqual(code, 0, out)
        self.assertIn('Ready to start (0):', out)
        self.assertIn("unknown state 'claimd'", out)
        code, out = self.fx.run('claim', 'ADOPT.01', '--worker', 'w1')
        self.assertEqual(code, 1, out)
        naive = dict(self.fx.claim_data('ADOPT.02'), leaseUntil='2026-09-30T00:00:00')
        rec = d.Record('claims', 'adopt-02', 'ADOPT.02', '0' * 40, naive, d.record_errors('claims', 'ADOPT.02', naive))
        self.assertEqual(rec.availability(d.utcnow()), 'invalid')
        self.assertIn('leaseUntil has no timezone: 2026-09-30T00:00:00', rec.errors)

    # ---- claims: creation, compare-and-swap, ownership and epochs (finding 1) ----------------

    def test_claim_is_exclusive_and_race_safe(self):
        self.assertEqual(self.fx.run('claim', 'ADOPT.01', '--worker', 'w1')[0], 0)
        code, out = self.fx.run('claim', 'ADOPT.01', '--worker', 'w2', plan=self.fx.plan2)
        self.assertEqual(code, 2, out)
        self.assertIn('is held', out)
        # A creation based on an observation made before the branch existed is refused.
        with self.assertRaises(d.Conflict):
            d.push_record(self.fx.plan2, 'claims', 'adopt-01', self.fx.claim_data('ADOPT.01', 'w2'), None, 'late create')

    def test_writes_bind_to_the_exact_observed_commit(self):
        self.assertEqual(self.fx.run('claim', 'ADOPT.01', '--worker', 'w1')[0], 0)
        seen = d.observe(self.fx.plan2, 'claims', 'adopt-01', 'ADOPT.01')
        self.assertEqual(self.fx.run('update', 'ADOPT.01', '--worker', 'w1', '--epoch', '1', '--done', 'x')[0], 0)
        stale = dict(seen.data, epoch=2, claimant='w2')
        with self.assertRaises(d.Conflict):
            d.push_record(self.fx.plan2, 'claims', 'adopt-01', stale, seen.sha, 'stale takeover')
        now = d.observe(self.fx.plan, 'claims', 'adopt-01', 'ADOPT.01')
        self.assertEqual((now.data['claimant'], now.data['epoch']), ('w1', 1))

    def test_only_the_claimant_at_the_current_epoch_changes_a_claim(self):
        self.assertEqual(self.fx.run('claim', 'ADOPT.01', '--worker', 'w1')[0], 0)
        self.assertEqual(self.fx.run('update', 'ADOPT.01', '--worker', 'w2', '--epoch', '1')[0], 2)
        self.assertEqual(self.fx.run('update', 'ADOPT.01', '--worker', 'w1', '--epoch', '2')[0], 2)
        self.assertEqual(self.fx.run('release', 'ADOPT.01', '--worker', 'w2', '--epoch', '1', '--note', 'no')[0], 2)
        sha = '1' * 40
        code, out = self.fx.run('update', 'ADOPT.01', '--worker', 'w1', '--epoch', '1', '--branch', 'task/adopt-01',
                                '--pr', 'https://example.invalid/pull/1', '--head', sha, '--next', 'review')
        self.assertEqual(code, 0, out)
        rec = d.observe(self.fx.plan, 'claims', 'adopt-01', 'ADOPT.01')
        self.assertEqual(rec.data['handoff']['head'], sha)
        self.assertEqual(rec.data['handoff']['prs'], ['https://example.invalid/pull/1'])
        self.assertEqual(rec.data['handoff']['next'], ['review'])
        self.assertEqual(self.fx.run('update', 'ADOPT.01', '--worker', 'w1', '--epoch', '1', '--state', 'blocked')[0], 1)
        self.assertEqual(self.fx.run('update', 'ADOPT.01', '--worker', 'w1', '--epoch', '1', '--state', 'blocked',
                                     '--blocker', 'waiting for a provider account')[0], 0)
        code, out = self.fx.run('status')
        self.assertIn('BLOCKER: waiting for a provider account', out)
        self.assertEqual(self.fx.run('update', 'ADOPT.01', '--worker', 'w1', '--epoch', '1', '--state', 'claimed')[0], 0)
        self.assertIsNone(d.observe(self.fx.plan, 'claims', 'adopt-01', 'ADOPT.01').data['handoff']['blocker'])

    def test_release_then_reclaim_advances_the_epoch_and_fences_the_old_holder(self):
        self.assertEqual(self.fx.run('claim', 'ADOPT.01', '--worker', 'w1')[0], 0)
        self.assertEqual(self.fx.run('release', 'ADOPT.01', '--worker', 'w1', '--epoch', '1', '--note', 'handoff: half done',
                                     '--next', 'finish the record')[0], 0)
        code, out = self.fx.run('ready')
        self.assertIn('resume the released work', out)
        code, out = self.fx.run('claim', 'ADOPT.01', '--worker', 'w2', plan=self.fx.plan2)
        self.assertEqual(code, 0, out)
        rec = d.observe(self.fx.plan, 'claims', 'adopt-01', 'ADOPT.01')
        self.assertEqual((rec.data['claimant'], rec.data['epoch']), ('w2', 2))
        self.assertEqual(rec.data['handoff']['next'], ['finish the record'])
        self.assertEqual(self.fx.run('update', 'ADOPT.01', '--worker', 'w1', '--epoch', '1')[0], 2)

    def test_takeover_needs_expiry_grace_and_a_reason(self):
        self.fx.raw_claim('ADOPT.01', self.fx.claim_data('ADOPT.01', lease_hours=-0.5))
        self.assertEqual(self.fx.run('claim', 'ADOPT.01', '--worker', 'w2', '--takeover', '--reason', 'r')[0], 2)
        rec = d.observe(self.fx.plan, 'claims', 'adopt-01', 'ADOPT.01')
        expired = dict(self.fx.claim_data('ADOPT.01', lease_hours=-3), epoch=1)
        d.push_record(self.fx.plan, 'claims', 'adopt-01', expired, rec.sha, 'expire')
        code, out = self.fx.run('claim', 'ADOPT.01', '--worker', 'w2')
        self.assertEqual(code, 2, out)
        self.assertIn('recovery', out)
        self.assertEqual(self.fx.run('claim', 'ADOPT.01', '--worker', 'w2', '--takeover')[0], 1)
        code, out = self.fx.run('claim', 'ADOPT.01', '--worker', 'w2', '--takeover', '--reason',
                                'branch and PR idle since expiry; release request unanswered for 1 hour')
        self.assertEqual(code, 0, out)
        rec = d.observe(self.fx.plan, 'claims', 'adopt-01', 'ADOPT.01')
        self.assertEqual((rec.data['claimant'], rec.data['epoch']), ('w2', 2))
        self.assertIn('takeover from ghost epoch 1', rec.data['handoff']['note'])

    # ---- completion and follow-up (finding 3) ------------------------------------------------

    def test_completion_is_recorded_only_after_the_ledger(self):
        self.assertEqual(self.fx.run('claim', 'ADOPT.01', '--worker', 'w1')[0], 0)
        self.assertEqual(self.fx.run('update', 'ADOPT.01', '--worker', 'w1', '--epoch', '1', '--state', 'complete')[0], 1)
        self.fx.record('ADOPT.01', 'complete')
        self.fx.commit(self.fx.plan, 'ledger')
        self.assertEqual(self.fx.run('update', 'ADOPT.01', '--worker', 'w1', '--epoch', '1', '--state', 'complete')[0], 0)
        code, out = self.fx.run('ready')
        self.assertIn('Ready to start (58):', out)
        self.assertNotIn('ADOPT.01\t', out)

    def test_complete_ledger_requires_completed_integration_prerequisites(self):
        g = d.Graph(self.fx.design)
        self.fx.record('AND.08', 'complete')  # AND.07 is its completion prerequisite
        self.fx.record('AND.13', 'inherited')  # AND.08 also completes on AND.13 (UI suite); inherited carries no evidence rules
        for status in (None, 'delivered', 'superseded'):
            with self.subTest(prerequisite=status):
                if status:
                    self.fx.record('AND.07', status)
                _, errors = d.read_ledger(self.fx.plan, g)
                self.assertTrue(any('AND.08 cannot be complete' in e and 'AND.07' in e for e in errors), errors)
        # Both the working-tree check and authoritative readiness use this validation.
        code, out = self.fx.run('check')
        self.assertEqual(code, 1, out)
        self.assertIn('AND.08 cannot be complete', out)
        self.fx.commit(self.fx.plan, 'invalid premature completion')
        code, out = self.fx.run('ready')
        self.assertEqual(code, 1, out)
        self.assertIn('AND.08 cannot be complete', out)
        for status in ('complete', 'inherited'):
            self.fx.record('AND.07', status)
            _, errors = d.read_ledger(self.fx.plan, g)
            self.assertEqual(errors, [])
        # Delivered work and adopted inherited work need not have completed these scenarios yet.
        self.fx.record('AND.07', 'delivered')
        for status in ('delivered', 'inherited'):
            self.fx.record('AND.08', status)
            self.assertEqual(d.read_ledger(self.fx.plan, g)[1], [])

    def test_repository_adoption_completion_requires_every_generated_slice(self):
        g = d.Graph(self.fx.design)
        self.fx.record('ADOPT.02', 'complete')
        slices = [e['task'] for e in g.tasks['ADOPT.02']['complete']]
        self.assertTrue(slices)
        for sid in slices[:-1]:
            self.fx.record(sid, 'complete')
        _, errors = d.read_ledger(self.fx.plan, g)
        self.assertTrue(any('ADOPT.02 cannot be complete' in e and slices[-1] in e for e in errors), errors)
        self.fx.record(slices[-1], 'complete')
        self.assertEqual(d.read_ledger(self.fx.plan, g)[1], [])

    def test_a_delivered_task_returns_as_a_follow_up_when_its_completion_prerequisites_complete(self):
        self.fx.record('AND.08', 'delivered')
        self.fx.record('AND.13', 'inherited')  # the second completion prerequisite of AND.08 in the current graph
        self.fx.commit(self.fx.plan, 'delivered')
        code, out = self.fx.run('status')
        self.assertIn('AND.08\twaiting for AND.07', out)
        code, out = self.fx.run('ready')
        self.assertIn('completion follow-ups (0)', out)
        self.fx.record('AND.07', 'complete')
        self.fx.commit(self.fx.plan, 'prerequisite complete')
        code, out = self.fx.run('ready')
        self.assertIn('completion follow-ups (1):', out)
        self.assertIn('AND.08\tMobile', out)
        code, out = self.fx.run('claim', 'AND.08', '--worker', 'w3')
        self.assertEqual(code, 0, out)
        self.assertIn('Follow up succeeded', out)
        self.assertEqual(self.fx.run('claim', 'AND.09', '--worker', 'w3')[0], 2)

    # ---- adoption records every inherited task (Design adoption stage, section 3) ------------

    def test_each_task_a_slice_classifies_as_inherited_gets_its_own_record(self):
        g = d.Graph(self.fx.design)
        for sid in g.slices:
            prompt = '\n'.join(d.render_slice_prompt(g, sid, 'D', 'P'))
            scope = next(ln for ln in prompt.splitlines() if ln.startswith('Permitted write scope: '))
            self.assertIn(f'Plan:ledger/tasks/{d.key_of(sid)}.md', scope)
            self.assertIn('Plan:ledger/tasks/<key>.md (status inherited)', scope)
            for tid in g.slice_tasks(sid):
                if g.tasks[tid]['baseline']['state'] == 'accepted':
                    self.assertIn(f'Plan:ledger/tasks/{d.key_of(tid)}.md', scope)
        # The governance slice classifies GOV.17 as inherited: without its record the merged slice makes it ready.
        for task, status in (('ADOPT.01', 'complete'), ('ADOPT.02.governance', 'complete'), ('GOV.01', 'inherited'),
                             ('GOV.02', 'inherited'), ('GOV.03', 'inherited')):
            self.fx.record(task, status)
        self.fx.commit(self.fx.plan, 'governance slice')
        code, out = self.fx.run('ready', '--lane', 'governance')
        self.assertIn('GOV.17\tDesktopPlatform', out)
        self.fx.record('GOV.17', 'inherited')
        self.fx.record('CON.23', 'delivered')  # GOV.18 starts on the delivered CON.23 naming data in the current graph
        self.fx.commit(self.fx.plan, 'inherited record')
        code, out = self.fx.run('ready', '--lane', 'governance')
        self.assertEqual(code, 0, out)
        # GOV.04 edits retired policy bindings, so it waits for the GOV.18 cleanup (Design ADP-10).
        self.assertIn('Ready to start (1):', out)
        self.assertIn('GOV.18\tDesktopPlatform', out)
        self.assertNotIn('GOV.04\t', out)
        self.assertNotIn('GOV.17\t', out)

    # ---- adoption slices retired by a recorded decision (P2-021) ------------------------------

    def graph_with_slice(self, sid, design=None, **fields):
        """The Design graph with one adoption slice added or changed in memory; fields override its keys."""
        g = d.Graph(design or self.fx.design)
        base = g.slices.get(sid, {'id': sid, 'repo': 'Design', 'lane': 'governance', 'adoptionTask': 'ADOPT.11',
                                  'title': 'Governance slice with no tasks'})
        g.slices[sid] = dict(base, **fields)
        return g

    def test_a_retired_adoption_slice_with_no_tasks_is_valid_and_shows_as_retired(self):
        g = self.graph_with_slice('ADOPT.11.governance', retired=True, retiredBy='P2-022')
        self.assertEqual(d.validate(g)[0], [])
        # Rendering resolves decision IDs against the whole Design checkout, not the planning-only fixture.
        g = self.graph_with_slice('ADOPT.11.governance', design=DESIGN_SOURCE, retired=True, retiredBy='P2-022')
        self.assertIn('none (retired by P2-022)', d.render_lane(g, g.lanes['adoption']))

    def test_a_retired_adoption_slice_must_name_its_decision(self):
        for fields in ({'retired': True}, {'retired': True, 'retiredBy': None}, {'retired': True, 'retiredBy': ''}, {'retired': True, 'retiredBy': '  '}):
            with self.subTest(fields=fields):
                errors = d.validate(self.graph_with_slice('ADOPT.11.governance', **fields))[0]
                self.assertIn('ADOPT.11.governance: retired adoption slice must name its retiredBy decision', errors)

    def test_a_retired_adoption_slice_that_still_has_tasks_is_an_error(self):
        g = self.graph_with_slice('ADOPT.02.governance', retired=True, retiredBy='P2-022')
        self.assertIn('retired adoption slice for DesktopPlatform/governance still has tasks', d.validate(g)[0])

    def test_a_non_retired_adoption_slice_with_no_tasks_still_errors(self):
        for fields in ({}, {'retired': False, 'retiredBy': 'P2-022'}):
            with self.subTest(fields=fields):
                errors = d.validate(self.graph_with_slice('ADOPT.11.governance', **fields))[0]
                self.assertIn('adoption slice for Design/governance has no tasks', errors)

    # ---- authoritative state and worktrees (finding 7) ----------------------------------------

    def test_unmerged_checkout_changes_never_count(self):
        self.fx.record('ADOPT.01', 'complete')
        sh(self.fx.plan, 'add', '-A')
        sh(self.fx.plan, 'commit', '--quiet', '-m', 'local only')
        code, out = self.fx.run('ready')
        self.assertIn('Ready to start (1):', out)
        code, out = self.fx.run('ready', '--local')
        self.assertIn('UNREVIEWED LOCAL STATE', out)
        self.assertIn('Ready to start (58):', out)

    def test_default_design_is_the_same_from_a_worktree(self):
        primary = self.fx.root / 'primary' / 'Plan'
        sh(self.fx.root, 'clone', '--quiet', str(self.fx.root / 'plan.git'), str(primary))
        sh(primary, 'worktree', 'add', '--quiet', '-b', 'side', str(primary / '.worktree' / 'side'))
        saved, os.environ['ARCFORGES_DESIGN'] = os.environ.get('ARCFORGES_DESIGN'), ''
        saved_root = d.PLAN_ROOT
        try:
            os.environ.pop('ARCFORGES_DESIGN')
            d.PLAN_ROOT = primary / '.worktree' / 'side'
            self.assertEqual(d.default_design().resolve(), (self.fx.root / 'primary' / 'ArcForges-Design').resolve())
            os.environ['ARCFORGES_DESIGN'] = str(self.fx.design)
            self.assertEqual(d.default_design(), self.fx.design)
        finally:
            d.PLAN_ROOT = saved_root
            if saved is None:
                os.environ.pop('ARCFORGES_DESIGN', None)
            else:
                os.environ['ARCFORGES_DESIGN'] = saved

    def test_keys_are_windows_safe(self):
        self.assertEqual(d.key_of('CON.02'), 'con-02')
        self.assertEqual(d.key_of('ADOPT.03.contracts'), 'adopt-03-contracts')
        d.push_record(self.fx.plan, 'claims', 'con-02', self.fx.claim_data('CON.02'), None, 'reserved-name check')
        sh(self.fx.plan, 'branch', 'task/con-02')
        (self.fx.plan / 'ledger' / 'tasks' / 'con-02.md').write_text(ledger_text('CON.02', 'delivered'), encoding='utf-8')
        sh(self.fx.plan, 'add', 'ledger/tasks/con-02.md')

    # ---- leases, roles and the workstation build slot (findings 4 and 6) -----------------------

    def test_a_lease_needs_a_live_claim_on_its_task(self):
        self.assertEqual(self.fx.run('claim', 'RES-cloud-deployment', '--worker', 'w1', '--task', 'ADOPT.01')[0], 2)
        self.assertEqual(self.fx.run('claim', 'ADOPT.01', '--worker', 'w1')[0], 0)
        code, out = self.fx.run('claim', 'RES-cloud-deployment', '--worker', 'w1', '--task', 'ADOPT.01', '--hours', '1')
        self.assertEqual(code, 0, out)
        self.assertEqual(self.fx.run('claim', 'RES-cloud-deployment', '--worker', 'w2', '--task', 'ADOPT.01')[0], 2)
        self.assertEqual(self.fx.run('release', 'RES-cloud-deployment', '--worker', 'w1', '--epoch', '1',
                                     '--note', 'live run finished')[0], 0)

    def test_integration_role_is_discoverable_and_transferable(self):
        self.assertEqual(self.fx.run('claim', 'integration:Contracts', '--worker', 'w1')[0], 0)
        code, out = self.fx.run('status')
        self.assertIn('integration:Contracts\tclaimed by w1 epoch 1', out)
        self.assertNotIn('integration:Contracts,', out.split('Vacant integration roles:')[1].split('\n')[0])
        self.assertEqual(self.fx.run('claim', 'integration:Contracts', '--worker', 'w2')[0], 2)
        self.assertEqual(self.fx.run('release', 'integration:Contracts', '--worker', 'w1', '--epoch', '1',
                                     '--note', 'queue empty')[0], 0)
        self.assertEqual(self.fx.run('claim', 'integration:Contracts', '--worker', 'w2')[0], 0)

    def test_build_slot_is_exclusive_recoverable_and_released(self):
        os.environ['ARCFORGES_BUILD_SLOT'] = str(self.fx.root / 'slot' / 'build-slot')
        try:
            code = d.main(['build-slot', 'run', '--worker', 'w1', '--task', 'ADOPT.01', '--',
                           sys.executable, '-c', 'import sys; sys.exit(3)'])
            self.assertEqual(code, 3)
            self.assertFalse(d.slot_path().exists())
            if os.name == 'nt':  # a batch file named without a path runs from the current directory
                (self.fx.root / 'probe.bat').write_bytes(b'@exit /b 4\r\n')
                here = os.getcwd()
                os.chdir(self.fx.root)
                try:
                    self.assertEqual(d.main(['build-slot', 'run', '--worker', 'w1', '--task', 'ADOPT.01', '--', 'probe.bat']), 4)
                finally:
                    os.chdir(here)
            token = d.slot_acquire('w1', 'ADOPT.01', 60, 0, 'build')
            with self.assertRaises(d.Conflict):
                d.slot_acquire('w2', 'ADOPT.02', 60, 0, 'build')
            owner = d.slot_owner(d.slot_path())
            owner['expiresAt'] = d.iso(d.utcnow() - timedelta(minutes=5))
            d.slot_write(d.slot_path(), owner)
            second = d.slot_acquire('w2', 'ADOPT.02', 60, 0, 'build')
            self.assertEqual(d.slot_owner(d.slot_path())['worker'], 'w2')
            d.slot_release(token)  # the stale holder's release must not free the new holder's lock
            self.assertEqual(d.slot_owner(d.slot_path())['worker'], 'w2')
            d.slot_release(second)
            self.assertFalse(d.slot_path().exists())
        finally:
            os.environ.pop('ARCFORGES_BUILD_SLOT', None)

    def test_stale_build_slot_recovery_serializes_competing_waiters(self):
        with patch.dict(os.environ, {'ARCFORGES_BUILD_SLOT': str(self.fx.root / 'contended-slot')}):
            old = d.slot_acquire('old', 'ADOPT.01', 60, 0, 'build')
            owner = d.slot_owner(d.slot_path())
            owner['expiresAt'] = d.iso(d.utcnow() - timedelta(minutes=5))
            d.slot_write(d.slot_path(), owner)
            recovering, resume, attempting = threading.Event(), threading.Event(), threading.Event()
            second_observed = threading.Event()
            results, failures = {}, []
            discard, read_owner = d.slot_discard, d.slot_owner

            def observed_owner(path):
                if threading.current_thread().name == 'second':
                    second_observed.set()
                return read_owner(path)

            def paused_discard(path, label, *args, **kwargs):
                if label == 'stale' and threading.current_thread().name == 'first':
                    recovering.set()
                    if not resume.wait(10):
                        raise AssertionError('test did not release stale recovery')
                return discard(path, label, *args, **kwargs)

            def acquire(name):
                try:
                    if name == 'second':
                        attempting.set()
                    results[name] = d.slot_acquire(name, 'ADOPT.01', 60, 0, 'build')
                except d.Conflict:
                    results[name] = None
                except BaseException as exc:
                    failures.append(exc)

            first = threading.Thread(target=acquire, args=('first',), name='first')
            second = threading.Thread(target=acquire, args=('second',), name='second')
            with patch.object(d, 'slot_discard', side_effect=paused_discard), \
                    patch.object(d, 'slot_owner', side_effect=observed_owner):
                try:
                    first.start()
                    self.assertTrue(recovering.wait(10))  # old owner observed; removal deliberately paused
                    second.start()
                    self.assertTrue(attempting.wait(10))
                    self.assertFalse(second_observed.wait(0.2))  # inspection waits for the whole recovery
                finally:
                    resume.set()
                    first.join(10)
                    if second.ident is not None:
                        second.join(10)
            self.assertFalse(first.is_alive())
            self.assertFalse(second.is_alive())
            self.assertEqual(failures, [])
            self.assertIsNotNone(results['first'])
            self.assertIsNone(results['second'])
            fresh = d.slot_owner(d.slot_path())
            d.slot_release(old)
            d.slot_renew(old, 1)
            self.assertEqual(d.slot_owner(d.slot_path()), fresh)
            self.assertEqual(d.main(['build-slot', 'release', '--worker', 'old']), 2)
            self.assertEqual(d.slot_owner(d.slot_path()), fresh)
            d.slot_renew(results['first'], 120)
            self.assertGreater(d.slot_owner(d.slot_path())['expiresAt'], fresh['expiresAt'])
            self.assertEqual(d.main(['build-slot', 'release', '--worker', 'first']), 0)
            self.assertFalse(d.slot_path().exists())
            self.assertTrue(d.slot_path().with_name(d.slot_path().name + '.guard').is_file())

    def test_build_slot_guard_excludes_another_process_and_survives_release(self):
        path = self.fx.root / 'process-slot'
        script = ('import sys; from pathlib import Path; '
                  f'sys.path.insert(0, {str(Path(d.__file__).parent)!r}); import delivery as d; '
                  'print("attempting", flush=True)\n'
                  'with d.slot_guard(Path(sys.argv[1])): print("acquired", flush=True)\n')
        with d.slot_guard(path):
            child = subprocess.Popen([sys.executable, '-B', '-c', script, str(path)],
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            try:
                self.assertEqual(child.stdout.readline().strip(), 'attempting')
                with self.assertRaises(subprocess.TimeoutExpired):
                    child.communicate(timeout=0.2)
            except BaseException:
                child.kill()
                child.communicate()
                raise
        try:
            out, err = child.communicate(timeout=10)
        except BaseException:
            child.kill()
            child.communicate()
            raise
        self.assertEqual(child.returncode, 0, err)
        self.assertEqual(out.strip(), 'acquired')
        self.assertTrue(path.with_name(path.name + '.guard').is_file())


def load_graph_json(design: Path) -> dict:
    return json.loads((design / d.GRAPH_REL).read_text(encoding='utf-8'))


def free_tasks(g, count: int) -> list[str]:
    """The first count open in-scope tasks that nothing depends on and that take no part in gates, substitutes,
    shared resources or package acceptance, so a test may add edges between them without other effects."""
    succ = g.succ_map()
    gated = {t for rec in g.gates.values() for t in rec.get('tasks', [])}
    subbed = set()
    for s in g.subs.values():
        rp = s['realProducer'] if isinstance(s['realProducer'], list) else [s['realProducer']]
        subbed |= set(rp) | {s['replacedBy']}
    found = []
    for tid in sorted(g.tasks):
        t = g.tasks[tid]
        if t.get('slice') or t.get('kind') == 'adoption' or t.get('packageAcceptance'):
            continue
        if t['baseline']['state'] == 'accepted' or tid in gated or tid in subbed or succ.get(tid):
            continue
        if t.get('shared') or t.get('substitutes'):
            continue
        found.append(tid)
        if len(found) == count:
            return found
    raise AssertionError(f'fewer than {count} free tasks')


def pick_candidate(g) -> str:
    """An in-scope task that nothing depends on: no in-scope task, gate, substitute or shared resource uses it,
    it is not a package acceptance task, and it maps at least one numbered substep."""
    succ = g.succ_map()
    gated = {t for rec in g.gates.values() for t in rec.get('tasks', [])}
    subbed = set()
    for s in g.subs.values():
        rp = s['realProducer'] if isinstance(s['realProducer'], list) else [s['realProducer']]
        subbed |= set(rp) | {s['replacedBy']}
    for tid in sorted(g.tasks, reverse=True):
        t = g.tasks[tid]
        if t.get('slice') or t.get('kind') == 'adoption':
            continue
        if t['baseline']['state'] == 'accepted' or tid in gated or tid in subbed or succ.get(tid):
            continue
        if t.get('shared') or t.get('substitutes'):
            continue
        if any(d.SUBSTEP.match(o['ref']) for o in t['obligations']):
            return tid
    raise AssertionError('no candidate task')


def other_task(g, exclude: str) -> str:
    """An open in-scope task other than exclude (baseline-accepted tasks are exempt from the edge rule)."""
    return next(t for t in g.tasks if t != exclude and not g.tasks[t].get('slice') and g.tasks[t]['kind'] != 'adoption'
                and g.tasks[t]['baseline']['state'] != 'accepted')


def setattr_task(data: dict, tid: str, key: str, value) -> None:
    """Set one field of a task in a graph dict (None is stored as-is, to test malformed shapes)."""
    next(t for t in data['tasks'] if t['id'] == tid)[key] = value


def mark_out(data: dict, tid: str, closeout: bool = False, by: str = 'P2-026', note: str = 'synthetic scope test') -> dict:
    """Declare tid out of scope in a graph dict, carrying every substep and package obligation that no in-scope
    task maps (the coordinator's obligation entries)."""
    task = next(t for t in data['tasks'] if t['id'] == tid)
    task['outOfScope'] = {'by': by, 'note': note, **({'closeout': True} if closeout else {})}
    covered = {o['ref'] for t in data['tasks'] if 'outOfScope' not in t for o in t.get('obligations', [])}
    rows = data.setdefault('outOfScopeObligations', [])
    for o in task['obligations']:
        ref = o['ref']
        if (d.SUBSTEP.match(ref) or d.POB_ID.match(ref)) and ref not in covered and not any(r['ref'] == ref for r in rows):
            rows.append({'ref': ref, 'by': by, 'note': 'carried by the excluded task'})
    return task


class OutOfScopeTests(unittest.TestCase):
    """Decision P2-026: out-of-scope tasks, obligations, gates and substitutes (scope rules A to F)."""

    @classmethod
    def setUpClass(cls):
        if not (DESIGN_SOURCE / d.GRAPH_REL).is_file():
            raise unittest.SkipTest(f'no Design checkout at {DESIGN_SOURCE}')

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix='delivery-scope-')
        self.fx = Fixture(Path(self.tmp))
        self.pristine = load_graph_json(self.fx.design)

    def tearDown(self):
        def unlock(func, path, _):  # Git marks object files read-only on Windows
            os.chmod(path, 0o700)
            func(path)
        shutil.rmtree(self.tmp, onexc=unlock) if sys.version_info >= (3, 12) else shutil.rmtree(self.tmp, onerror=unlock)

    def edit_graph(self, mutate, commit: bool = False) -> d.Graph:
        data = json.loads(json.dumps(self.pristine))  # every edit starts from the committed graph
        mutate(data)
        (self.fx.design / d.GRAPH_REL).write_text(json.dumps(data, indent=1), encoding='utf-8')
        if commit:
            self.fx.commit(self.fx.design, 'scope change')
        return d.Graph(self.fx.design)

    def candidate(self) -> str:
        return pick_candidate(d.Graph(self.fx.design))

    def use_full_design(self):
        """Render links against the whole Design checkout (decision records are outside docs/planning), as the
        real views are rendered; the fixture starts with docs/planning only."""
        for p in (DESIGN_SOURCE / 'docs').iterdir():
            if p.name == 'planning':
                continue
            if p.is_dir():
                shutil.copytree(p, self.fx.design / 'docs' / p.name, dirs_exist_ok=True)
            else:
                shutil.copy2(p, self.fx.design / 'docs' / p.name)
        self.fx.commit(self.fx.design, 'full design docs')

    # ---- absent means in scope; shape (rule 1) ------------------------------------------------

    def test_absent_declarations_mean_in_scope(self):
        g = d.Graph(self.fx.design)
        self.assertFalse(any(d.is_out(t) for t in g.data['tasks']))
        self.assertEqual(d.validate(g)[0], [])
        self.assertEqual(d.analysis(g)['outOfScopeTasks'], 0)

    def test_scope_declarations_have_a_valid_shape(self):
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        gate = g0.data['gates'][0]['gate']
        sub = g0.data['substitutes'][0]['id']
        ref = next(iter(g0.catalogue))
        cases = {
            'task without by': (lambda data: setattr_task(data, cand, 'outOfScope', {'note': 'x'}),
                                f'{cand}: outOfScope needs a non-empty by'),
            'task with blank note': (lambda data: setattr_task(data, cand, 'outOfScope', {'by': 'P2-026', 'note': '  '}),
                                     f'{cand}: outOfScope needs a non-empty note'),
            'task with text closeout': (lambda data: setattr_task(data, cand, 'outOfScope',
                                                                  {'by': 'P2-026', 'note': 'x', 'closeout': 'yes'}),
                                        f'{cand}: outOfScope closeout must be true or false'),
            'task with unknown field': (lambda data: setattr_task(data, cand, 'outOfScope',
                                                                  {'by': 'P2-026', 'note': 'x', 'extra': 1}),
                                        f'{cand}: outOfScope has unknown field extra'),
            'task with null declaration': (lambda data: setattr_task(data, cand, 'outOfScope', None),
                                           f'{cand}: outOfScope must be an object'),
            'gate without note': (lambda data: next(x for x in data['gates'] if x['gate'] == gate).update(
                outOfScope={'by': 'P2-026'}), f'gate {gate}: outOfScope needs a non-empty note'),
            'substitute without by': (lambda data: next(x for x in data['substitutes'] if x['id'] == sub).update(
                outOfScope={'note': 'x'}), f'{sub}: outOfScope needs a non-empty by'),
            'obligation entry without by': (lambda data: data.update(outOfScopeObligations=[{'ref': ref, 'note': 'x'}]),
                                            f'outOfScopeObligations {ref} needs a non-empty by'),
        }
        for name, (mutate, expected) in cases.items():
            with self.subTest(case=name):
                errors = d.validate(self.edit_graph(mutate))[0]
                self.assertTrue(any(expected in e for e in errors), errors)

    # ---- rule 2: in-scope tasks never depend on out-of-scope tasks ----------------------------

    def test_in_scope_task_may_not_depend_on_an_out_of_scope_task(self):
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        other = other_task(g0, cand)

        def mutate(data):
            mark_out(data, cand)
            t = next(x for x in data['tasks'] if x['id'] == other)
            t['start'].append({'type': 'artifact', 'task': cand, 'need': 'n', 'why': 'w'})
            t['complete'].append({'type': 'integration', 'task': cand, 'need': 'n', 'why': 'w'})
        errors = d.validate(self.edit_graph(mutate))[0]
        self.assertTrue(any(other in e and cand in e and 'start edge' in e for e in errors), errors)
        self.assertTrue(any(other in e and cand in e and 'complete edge' in e for e in errors), errors)

    def test_an_out_of_scope_task_may_depend_on_in_scope_tasks(self):
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        other = other_task(g0, cand)

        def mutate(data):
            task = mark_out(data, cand)
            task['complete'].append({'type': 'integration', 'task': other, 'need': 'n', 'why': 'w'})
        errors = d.validate(self.edit_graph(mutate))[0]
        self.assertEqual(errors, [])

    # ---- rule 3: obligation coverage -----------------------------------------------------------

    def test_obligations_only_an_out_of_scope_task_maps_need_an_entry(self):
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        sids = [o['ref'] for o in g0.tasks[cand]['obligations'] if d.SUBSTEP.match(o['ref'])]

        def bare(data):
            next(t for t in data['tasks'] if t['id'] == cand)['outOfScope'] = {'by': 'P2-026', 'note': 'x'}
        errors = d.validate(self.edit_graph(bare))[0]
        for sid in sids:
            self.assertTrue(any(f'substep {sid} is mapped only by out-of-scope tasks' in e for e in errors), errors)
        self.assertEqual(d.validate(self.edit_graph(lambda data: mark_out(data, cand)))[0], [])

    def test_an_entry_must_name_a_real_obligation_and_not_one_in_scope_covers(self):
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        # an open covering task: a baseline-accepted one is history and may sit beside an entry (S2, S16(a))
        in_scope_sid = next(o['ref'] for t in g0.data['tasks'] if t['id'] != cand and t['baseline']['state'] != 'accepted'
                            for o in t['obligations'] if d.SUBSTEP.match(o['ref']))

        def mutate(data):
            mark_out(data, cand)
            data['outOfScopeObligations'].append({'ref': 'WP-99.99', 'by': 'P2-026', 'note': 'x'})
            data['outOfScopeObligations'].append({'ref': in_scope_sid, 'by': 'P2-026', 'note': 'x'})
        errors = d.validate(self.edit_graph(mutate))[0]
        self.assertTrue(any('outOfScopeObligations WP-99.99: not an active substep or package obligation' in e
                            for e in errors), errors)
        self.assertTrue(any(f'outOfScopeObligations {in_scope_sid}: also covered by an in-scope task that is not complete'
                            in e
                            for e in errors), errors)

    def test_an_excluded_obligation_must_still_map_to_a_task(self):  # N1: DLV-43 keeps excluded obligations mapped
        g0 = d.Graph(self.fx.design)
        om = g0.obligation_map()
        tid, ref = next((t['id'], o['ref']) for t in g0.data['tasks'] if len(t['obligations']) > 1
                        and not t.get('slice') and t['kind'] != 'adoption' for o in t['obligations']
                        if d.SUBSTEP.match(o['ref']) and len(om[o['ref']]) == 1)

        def unmapped(data):  # the only mapping goes; the entry carries the obligation with no task at all
            next(t for t in data['tasks'] if t['id'] == tid)['obligations'] = [
                o for o in next(t for t in data['tasks'] if t['id'] == tid)['obligations'] if o['ref'] != ref]
            data['outOfScopeObligations'] = [{'ref': ref, 'by': 'P2-026', 'note': 'x'}]
        errors = d.validate(self.edit_graph(unmapped))[0]
        self.assertTrue(any(f'outOfScopeObligations {ref}: no task maps it' in e for e in errors), errors)

    def test_count_wording_agrees_with_the_count(self):  # N6: generated views say 1 task and 2 tasks
        self.assertEqual(d.count_of(1, 'delivery task'), '1 delivery task')
        self.assertEqual(d.count_of(2, 'delivery task'), '2 delivery tasks')
        self.assertEqual(d.count_of(0, 'obligation'), '0 obligations')

    def test_an_entry_may_sit_beside_only_a_history_covering_task(self):
        # S2 and DLV-43: an excluded part of a complete task keeps its task-level text, and the entry records that it is
        # no longer required. A covering task that is still live (open or delivered) must not share the entry.
        g0 = d.Graph(self.fx.design)
        cover = pick_candidate(g0)
        ref = next(o['ref'] for o in g0.tasks[cover]['obligations'] if d.SUBSTEP.match(o['ref']))
        msg = f'outOfScopeObligations {ref}: also covered by an in-scope task that is not complete'

        def entry(data):
            data['outOfScopeObligations'] = [{'ref': ref, 'by': 'P2-026', 'note': 'excluded part of a complete task'}]
        g = self.edit_graph(entry)
        for statuses in ({}, {cover: 'delivered'}):
            with self.subTest(statuses=statuses):
                errors = d.validate(g, statuses)[0]
                self.assertTrue(any(msg in e for e in errors), errors)
        for statuses in ({cover: 'complete'}, {cover: 'inherited'}, {cover: 'superseded'}):  # N2: as the edge rule does
            with self.subTest(statuses=statuses):
                errors = d.validate(g, statuses)[0]
                self.assertFalse(any(f'{ref}: also covered' in e for e in errors), errors)

        def accepted(data):
            entry(data)
            next(t for t in data['tasks'] if t['id'] == cover)['baseline'] = {'state': 'accepted', 'evidence': 'synthetic'}
        errors = d.validate(self.edit_graph(accepted))[0]  # baseline acceptance is history without a ledger record
        self.assertFalse(any(f'{ref}: also covered' in e for e in errors), errors)

    def test_check_passes_with_an_excluded_part_of_a_complete_task(self):
        self.use_full_design()
        g0 = d.Graph(self.fx.design)
        succ = g0.succ_map()
        cover = next(t for t in sorted(g0.tasks) if not g0.tasks[t].get('slice') and g0.tasks[t]['kind'] != 'adoption'
                     and not g0.tasks[t]['complete'] and g0.tasks[t]['baseline']['state'] != 'accepted'
                     and not succ.get(t) and any(d.SUBSTEP.match(o['ref']) for o in g0.tasks[t]['obligations']))
        ref = next(o['ref'] for o in g0.tasks[cover]['obligations'] if d.SUBSTEP.match(o['ref']))

        def entry(data):
            data['outOfScopeObligations'] = [{'ref': ref, 'by': 'P2-026', 'note': 'excluded part of a complete task'}]
        self.edit_graph(entry, commit=True)
        self.fx.record(cover, 'complete')
        self.fx.commit(self.fx.plan, 'complete task with an excluded part')
        self.assertEqual(self.fx.run('generate')[0], 0)
        code, out = self.fx.run('check')
        self.assertEqual(code, 0, out)
        trace = (self.fx.design / d.DELIVERY_REL / 'traceability.md').read_text(encoding='utf-8')
        self.assertIn('Out of scope (P2-026): excluded part of a complete task', trace)

    # ---- rule 4: gates and substitutes ---------------------------------------------------------

    def test_an_in_scope_gate_or_substitute_may_not_name_an_out_of_scope_task(self):
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        gate = g0.data['gates'][0]['gate']
        sub = g0.data['substitutes'][0]['id']

        def mutate(data):
            mark_out(data, cand)
            next(x for x in data['gates'] if x['gate'] == gate)['tasks'].append(cand)
            next(x for x in data['substitutes'] if x['id'] == sub)['realProducer'] = [cand]
        errors = d.validate(self.edit_graph(mutate))[0]
        self.assertIn(f'gate {gate}: in-scope gate lists out-of-scope task {cand} (scope rule 4)', errors)
        self.assertIn(f'{sub}: in-scope substitute names out-of-scope task {cand}', errors)

        def out_of_scope_gate(data):
            mutate(data)
            next(x for x in data['gates'] if x['gate'] == gate)['outOfScope'] = {'by': 'P2-026', 'note': 'x'}
            next(x for x in data['substitutes'] if x['id'] == sub)['outOfScope'] = {'by': 'P2-026', 'note': 'x'}
        errors = d.validate(self.edit_graph(out_of_scope_gate))[0]
        self.assertFalse(any(f'gate {gate}: in-scope gate' in e for e in errors), errors)
        self.assertFalse(any(f'{sub}: in-scope substitute' in e for e in errors), errors)

    def test_an_out_of_scope_consumer_does_not_bind_its_substitute_removal(self):
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        sub = g0.data['substitutes'][0]['id']

        def mutate(data):
            mark_out(data, cand)
            next(t for t in data['tasks'] if t['id'] == cand)['substitutes'] = [sub]
        errors = d.validate(self.edit_graph(mutate))[0]
        self.assertFalse(any(f'{sub}: replacing task' in e and cand in e for e in errors), errors)

    def test_an_in_scope_task_may_not_use_an_out_of_scope_substitute(self):
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        other = other_task(g0, cand)
        used = {s for t in g0.data['tasks'] for s in t.get('substitutes', [])}
        sub = next(s['id'] for s in g0.data['substitutes'] if s['id'] not in used)  # no in-scope task uses it yet

        def out_sub(data):
            next(x for x in data['substitutes'] if x['id'] == sub)['outOfScope'] = {'by': 'P2-026', 'note': 'x'}

        def mutate(data):
            out_sub(data)
            next(t for t in data['tasks'] if t['id'] == other)['substitutes'] = [sub]
        errors = d.validate(self.edit_graph(mutate))[0]
        self.assertIn(f'{other}: in-scope task uses out-of-scope substitute {sub}', errors)

        def out_consumer(data):  # an out-of-scope consumer, which nothing depends on, may use an out-of-scope substitute
            out_sub(data)
            mark_out(data, cand)
            next(t for t in data['tasks'] if t['id'] == cand)['substitutes'] = [sub]
        errors = d.validate(self.edit_graph(out_consumer))[0]
        self.assertFalse(any('uses out-of-scope substitute' in e for e in errors), errors)

        self.edit_graph(mutate, commit=True)  # the same refusal from check, as a planning change would meet it
        code, out = self.fx.run('check')
        self.assertNotEqual(code, 0, out)
        self.assertIn(f'{other}: in-scope task uses out-of-scope substitute {sub}', out)

    def test_an_out_of_scope_substitute_is_history_for_a_delivered_or_complete_user(self):  # S16(a)
        self.use_full_design()  # check resolves decision identifiers in the whole Design docs
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        used = {s for t in g0.data['tasks'] for s in t.get('substitutes', [])}
        sub = next(s['id'] for s in g0.data['substitutes'] if s['id'] not in used)
        rb = g0.subs[sub]['replacedBy']
        # A user the replacing task depends on, so the consumer rule does not bind and only the usage rule is under test.
        other = next(t for t in sorted(g0.tasks) if t != cand and t in g0.ancestors(rb)
                     and not g0.tasks[t].get('slice') and g0.tasks[t]['kind'] != 'adoption'
                     and g0.tasks[t]['baseline']['state'] != 'accepted')
        message = f'{other}: in-scope task uses out-of-scope substitute {sub}'

        def mutate(data):
            next(x for x in data['substitutes'] if x['id'] == sub)['outOfScope'] = {'by': 'P2-026', 'note': 'x'}
            next(t for t in data['tasks'] if t['id'] == other)['substitutes'] = [sub]
        g = self.edit_graph(mutate)
        for statuses in (None, {}, {other: None}):  # no ledger record: the task is open and the usage is refused
            with self.subTest(statuses=statuses):
                self.assertIn(message, d.validate(g, statuses)[0])
        for status in ('delivered', 'complete', 'inherited', 'superseded'):
            with self.subTest(status=status):
                self.assertNotIn(message, d.validate(g, {other: status})[0])

        def accepted(data):
            next(x for x in data['tasks'] if x['id'] == other)['baseline'] = {'state': 'accepted', 'evidence': 'synthetic'}
        g2 = self.edit_graph(lambda data: (mutate(data), accepted(data)))
        self.assertNotIn(message, d.validate(g2)[0])  # baseline acceptance exempts the usage without a ledger record

        self.edit_graph(mutate, commit=True)  # a delivered user passes check, as the S8 graph does once its ledger says so
        self.fx.record(other, 'delivered')
        self.fx.commit(self.fx.plan, 'delivered user of an out-of-scope substitute')
        self.assertEqual(self.fx.run('generate')[0], 0)
        code, out = self.fx.run('check')
        self.assertEqual(code, 0, out)
        self.assertNotIn(message, out)

    def out_substitute_user(self):
        """An unused substitute marked out of scope, and an in-scope task that the replacing task depends on, which
        uses it (so the consumer rule does not bind and only the usage rule is under test)."""
        g0 = d.Graph(self.fx.design)
        used = {s for t in g0.data['tasks'] for s in t.get('substitutes', [])}
        sub = next(s['id'] for s in g0.data['substitutes'] if s['id'] not in used)
        rb = g0.subs[sub]['replacedBy']
        cand = pick_candidate(g0)
        other = next(t for t in sorted(g0.tasks) if t != cand and t in g0.ancestors(rb)
                     and not g0.tasks[t].get('slice') and g0.tasks[t]['kind'] != 'adoption'
                     and g0.tasks[t]['baseline']['state'] != 'accepted')

        def mutate(data):
            next(x for x in data['substitutes'] if x['id'] == sub)['outOfScope'] = {'by': 'P2-026', 'note': 'x'}
            next(t for t in data['tasks'] if t['id'] == other)['substitutes'] = [sub]
        return sub, other, self.edit_graph(mutate)

    def test_an_open_user_of_an_out_of_scope_substitute_is_refused(self):  # M1, S16(a)
        sub, other, g = self.out_substitute_user()
        message = f'{other}: in-scope task uses out-of-scope substitute {sub}'
        for statuses in (None, {}, {other: None}, {other: 'not-a-status'}):
            with self.subTest(statuses=statuses):
                self.assertIn(message, d.validate(g, statuses)[0])

    def test_a_delivered_user_of_an_out_of_scope_substitute_is_history(self):  # M1, S16(a)
        sub, other, g = self.out_substitute_user()
        message = f'{other}: in-scope task uses out-of-scope substitute {sub}'
        self.assertNotIn(message, d.validate(g, {other: 'delivered'})[0])

    def test_a_complete_user_of_an_out_of_scope_substitute_is_history(self):  # M1, S16(a)
        sub, other, g = self.out_substitute_user()
        message = f'{other}: in-scope task uses out-of-scope substitute {sub}'
        self.assertNotIn(message, d.validate(g, {other: 'complete'})[0])

    def test_a_decision_anchor_is_read_from_the_checked_design_root(self):  # M2: DLV-43 sequencing
        cand = pick_candidate(d.Graph(self.fx.design))
        # Merged Design main has no P2-026 record: the committed fixture record goes, and that is pushed.
        (self.fx.design / 'docs' / 'decisions' / 'scope-record-fixture.md').unlink()
        self.fx.commit(self.fx.design, 'no decision record on merged main')
        self.assertEqual(sh(self.fx.design, 'ls-tree', '-r', '--name-only', 'origin/main', 'docs/decisions'), '')
        # The unmerged planning change adds the record and its markers together, in the checked root only.
        record = self.fx.design / 'docs' / 'decisions' / 'p2-026-unmerged.md'
        record.write_text('# P2-026 scope record (unmerged)\n\n<a id="rule-p2-026"></a>\n', encoding='utf-8')
        g = self.edit_graph(lambda data: mark_out(data, cand))
        self.assertFalse(any('names P2-026' in e for e in d.validate(g)[0]), d.validate(g)[0])
        # A missing anchor in the checked root is refused, whatever merged main says.
        record.unlink()
        errors = d.validate(d.Graph(self.fx.design))[0]
        self.assertTrue(any(f'{cand}: outOfScope names P2-026, which is not a scope decision record' in e
                            for e in errors), errors)

    # ---- rule 5: warnings ----------------------------------------------------------------------

    def test_warnings_for_resources_and_slices_used_only_out_of_scope(self):
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        sid = next(s for s in g0.slices if g0.slice_tasks(s))

        def mutate(data):
            data['sharedResources'].append({'id': 'RES-scope-test', 'title': 'Scope test', 'kind': 'file',
                                            'ownerRepo': 'multiple', 'owner': 'Plan', 'protocol': 'test'})
            mark_out(data, cand)
            next(t for t in data['tasks'] if t['id'] == cand)['shared'] = [{'resource': 'RES-scope-test', 'mode': 'read'}]
            for tid in g0.slice_tasks(sid):
                mark_out(data, tid)
        warnings = d.validate(self.edit_graph(mutate))[1]
        self.assertIn('RES-scope-test: shared resource used only by out-of-scope tasks', warnings)
        self.assertIn(f'{sid}: every task of this adoption slice is out of scope', warnings)

    # ---- rule 6: ledger records ----------------------------------------------------------------

    def test_out_of_scope_ledger_records_stay_valid_with_any_status(self):
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        other = other_task(g0, cand)

        def mutate(data):
            task = mark_out(data, cand)
            task['complete'].append({'type': 'integration', 'task': other, 'need': 'n', 'why': 'w'})
        g = self.edit_graph(mutate, commit=True)
        for status in ('complete', 'delivered', 'superseded', 'inherited'):
            with self.subTest(status=status):
                self.fx.record(cand, status)
                self.assertEqual(d.read_ledger(self.fx.plan, g)[1], [])

    # ---- rule C: scheduling, claims and status -------------------------------------------------

    def test_ready_and_status_never_list_out_of_scope_work(self):
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        other = other_task(g0, cand)

        def mutate(data):
            task = mark_out(data, cand)
            task['complete'].append({'type': 'integration', 'task': other, 'need': 'n', 'why': 'w'})
        self.edit_graph(mutate, commit=True)
        self.fx.record(cand, 'delivered')
        self.fx.commit(self.fx.plan, 'delivered out of scope')
        code, out = self.fx.run('ready')
        self.assertEqual(code, 0, out)
        self.assertNotIn(f'{cand}\t', out)
        self.assertIn('completion follow-ups (0)', out)
        code, out = self.fx.run('status')
        self.assertIn('Delivered tasks waiting for completion prerequisites (0):', out)

    def test_a_new_claim_on_an_out_of_scope_task_is_refused(self):
        cand = pick_candidate(d.Graph(self.fx.design))
        self.edit_graph(lambda data: mark_out(data, cand), commit=True)
        code, out = self.fx.run('claim', cand, '--worker', 'w1')
        self.assertEqual(code, 2, out)
        self.assertIn(f'{cand} is out of scope (P2-026): synthetic scope test', out)

    def test_live_claim_on_out_of_scope_task_is_listed_with_release_action(self):
        cand = pick_candidate(d.Graph(self.fx.design))
        self.edit_graph(lambda data: mark_out(data, cand), commit=True)
        self.fx.raw_claim(cand, self.fx.claim_data(cand, claimant='w1'))
        code, out = self.fx.run('status')
        self.assertEqual(code, 0, out)
        self.assertIn('Claims on out-of-scope tasks (1):', out)
        self.assertIn('action: release', out)
        code, out = self.fx.run('status', '--json')
        self.assertIn('"action": "release', out)

    def test_closeout_claim_is_finished_but_never_claimed_anew(self):
        cand = pick_candidate(d.Graph(self.fx.design))
        self.edit_graph(lambda data: mark_out(data, cand, closeout=True), commit=True)
        self.fx.raw_claim(cand, self.fx.claim_data(cand, claimant='w1'))
        code, out = self.fx.run('status')
        self.assertIn('action: finish under closeout', out)
        self.assertEqual(self.fx.run('update', cand, '--worker', 'w1', '--epoch', '1', '--done', 'finished evidence')[0], 0)
        self.assertEqual(self.fx.run('release', cand, '--worker', 'w1', '--epoch', '1', '--note', 'closeout done')[0], 0)
        code, out = self.fx.run('claim', cand, '--worker', 'w2', plan=self.fx.plan2)
        self.assertEqual(code, 2, out)
        self.assertIn('is out of scope', out)
        code, out = self.fx.run('show', cand)
        self.assertIn('closeout', out)

    def test_an_expired_claim_on_out_of_scope_task_is_listed_and_only_its_holder_releases_it(self):  # N3
        cand = pick_candidate(d.Graph(self.fx.design))
        self.edit_graph(lambda data: mark_out(data, cand), commit=True)
        # expired: the lease ended more than the one-hour grace ago
        self.fx.raw_claim(cand, self.fx.claim_data(cand, claimant='w1', lease_hours=1.0, age_hours=3.0))
        code, out = self.fx.run('status')
        self.assertEqual(code, 0, out)
        self.assertIn('Claims on out-of-scope tasks (1):', out)
        self.assertIn('action: release by the holder', out)
        code, out = self.fx.run('status', '--json')
        self.assertIn('"availability": "expired"', out)
        self.assertIn('"action": "release by the holder', out)
        # no other worker takes it over: a takeover of a non-closeout task is refused even after the grace
        code, out = self.fx.run('claim', cand, '--worker', 'w2', '--takeover', '--reason', 'idle', plan=self.fx.plan2)
        self.assertEqual(code, 2, out)
        self.assertIn('is out of scope', out)
        self.assertEqual(self.fx.run('release', cand, '--worker', 'w1', '--epoch', '1', '--note', 'stopped')[0], 0)
        code, out = self.fx.run('status')
        self.assertIn('Claims on out-of-scope tasks (0):', out)

    def test_an_expired_closeout_claim_is_taken_over_only_to_finish_its_closeout(self):  # N3, DLV-43 closeout
        cand = pick_candidate(d.Graph(self.fx.design))
        self.edit_graph(lambda data: mark_out(data, cand, closeout=True), commit=True)
        self.fx.raw_claim(cand, self.fx.claim_data(cand, claimant='w1', lease_hours=1.0, age_hours=3.0))
        code, out = self.fx.run('status')
        self.assertIn('take over under closeout', out)
        # the normal expiry rules still apply: without --takeover the expired claim is refused ...
        code, out = self.fx.run('claim', cand, '--worker', 'w2', plan=self.fx.plan2)
        self.assertEqual(code, 2, out)
        self.assertIn('expired claim', out)
        # ... and a takeover needs a reason
        self.assertEqual(self.fx.run('claim', cand, '--worker', 'w2', '--takeover', plan=self.fx.plan2)[0], 1)
        code, out = self.fx.run('claim', cand, '--worker', 'w2', '--takeover', '--reason', 'closeout after idle lease',
                                plan=self.fx.plan2)
        self.assertEqual(code, 0, out)
        rec = d.observe(self.fx.plan, 'claims', d.key_of(cand), cand)
        self.assertEqual((rec.data['claimant'], rec.data['epoch'], rec.data['state']), ('w2', 2, 'claimed'))
        code, out = self.fx.run('status')
        self.assertIn('finish under closeout', out)
        # the taker finishes the closeout; a later worker still cannot claim the task
        self.assertEqual(self.fx.run('release', cand, '--worker', 'w2', '--epoch', '2', '--note', 'closeout done')[0], 0)
        code, out = self.fx.run('claim', cand, '--worker', 'w3', plan=self.fx.plan2)
        self.assertEqual(code, 2, out)
        self.assertIn('is out of scope', out)

    def test_a_delivered_closeout_claim_is_listed_and_taken_over_to_finish_the_closeout(self):  # N3 (review b67c1e6)
        cand = pick_candidate(d.Graph(self.fx.design))
        self.edit_graph(lambda data: mark_out(data, cand, closeout=True), commit=True)
        self.fx.record(cand, 'delivered')
        self.fx.commit(self.fx.plan, 'delivered')
        self.fx.raw_claim(cand, self.fx.claim_data(cand, claimant='w1'))
        self.assertEqual(self.fx.run('update', cand, '--worker', 'w1', '--epoch', '1', '--state', 'delivered')[0], 0)
        # the delivered record holds no lease: it is listed with the takeover action, not invisible
        code, out = self.fx.run('status')
        self.assertIn('Claims on out-of-scope tasks (1):', out)
        self.assertIn('action: take over under closeout', out)
        code, out = self.fx.run('status', '--json')
        self.assertIn('"availability": "delivered"', out)
        self.assertIn('"action": "take over under closeout', out)
        # no plain claim, and the takeover needs a reason
        code, out = self.fx.run('claim', cand, '--worker', 'w2', plan=self.fx.plan2)
        self.assertEqual(code, 2, out)
        self.assertIn('delivered under its closeout', out)
        self.assertEqual(self.fx.run('claim', cand, '--worker', 'w2', '--takeover', plan=self.fx.plan2)[0], 1)
        code, out = self.fx.run('claim', cand, '--worker', 'w2', '--takeover', '--reason', 'closeout after delivery',
                                plan=self.fx.plan2)
        self.assertEqual(code, 0, out)
        rec = d.observe(self.fx.plan, 'claims', d.key_of(cand), cand)
        self.assertEqual((rec.data['claimant'], rec.data['epoch'], rec.data['state']), ('w2', 2, 'claimed'))
        self.assertIn('takeover from w1 epoch 1', rec.data['handoff']['note'])
        code, out = self.fx.run('status')
        self.assertIn('action: finish under closeout', out)
        # the taker finishes the closeout once the ledger records it complete; the claim then owes nothing
        self.fx.record(cand, 'complete')
        self.fx.commit(self.fx.plan, 'complete')
        self.assertEqual(self.fx.run('update', cand, '--worker', 'w2', '--epoch', '2', '--state', 'complete',
                                     plan=self.fx.plan2)[0], 0)
        code, out = self.fx.run('status')
        self.assertIn('Claims on out-of-scope tasks (1):', out)
        self.assertIn('none owed', out)
        code, out = self.fx.run('claim', cand, '--worker', 'w3', plan=self.fx.plan2)
        self.assertEqual(code, 2, out)
        self.assertIn('complete', out)

    def test_a_delivered_or_complete_claim_on_a_non_closeout_task_is_listed_and_owes_nothing(self):  # N3
        cand = pick_candidate(d.Graph(self.fx.design))
        self.edit_graph(lambda data: mark_out(data, cand), commit=True)
        delivered = self.fx.claim_data(cand, claimant='w1', state='delivered')
        pushed = self.fx.raw_claim(cand, delivered)
        code, out = self.fx.run('status')
        self.assertIn('Claims on out-of-scope tasks (1):', out)
        self.assertIn('action: none owed', out)
        # no closeout: nobody takes it over, and no plain claim is made
        code, out = self.fx.run('claim', cand, '--worker', 'w2', '--takeover', '--reason', 'idle', plan=self.fx.plan2)
        self.assertEqual(code, 1, out)
        code, out = self.fx.run('claim', cand, '--worker', 'w2', plan=self.fx.plan2)
        self.assertEqual(code, 2, out)
        self.assertIn('is out of scope', out)
        # the same claim recorded complete is listed too, still owing nothing
        complete = dict(delivered, state='complete')
        d.push_record(self.fx.plan, 'claims', d.key_of(cand), complete, pushed, 'complete')
        code, out = self.fx.run('status', '--json')
        self.assertIn('"availability": "complete"', out)
        self.assertIn('"action": "none owed', out)
        code, out = self.fx.run('claim', cand, '--worker', 'w2', '--takeover', '--reason', 'idle', plan=self.fx.plan2)
        self.assertEqual(code, 2, out)
        self.assertIn('is complete', out)

    # ---- S16(a): the edge rule follows the ledger status ----------------------------------------

    def edge_pair(self, extra=None):
        """Mark a candidate out and give another in-scope task a start and a complete edge to it."""
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        other = other_task(g0, cand)

        def mutate(data):
            mark_out(data, cand)
            t = next(x for x in data['tasks'] if x['id'] == other)
            t['start'].append({'type': 'artifact', 'task': cand, 'need': 'n', 'why': 'w'})
            t['complete'].append({'type': 'integration', 'task': cand, 'need': 'n', 'why': 'w'})
            if extra:
                extra(data)
        return cand, other, self.edit_graph(mutate)

    def test_an_open_task_may_not_start_or_complete_on_an_out_of_scope_task(self):
        cand, other, g = self.edge_pair()
        for statuses in (None, {}, {other: None}):  # no ledger record: the task is open
            with self.subTest(statuses=statuses):
                errors = d.validate(g, statuses)[0]
                self.assertTrue(any(f'{other}: start edge to out-of-scope task {cand}' in e for e in errors), errors)
                self.assertTrue(any(f'{other}: complete edge to out-of-scope task {cand}' in e for e in errors), errors)

    def test_a_delivered_task_keeps_its_start_edges_as_history_but_not_its_complete_edges(self):
        cand, other, g = self.edge_pair()
        errors = d.validate(g, {other: 'delivered'})[0]
        self.assertFalse(any(f'{other}: start edge to out-of-scope task' in e for e in errors), errors)
        self.assertTrue(any(f'{other}: complete edge to out-of-scope task {cand}' in e for e in errors), errors)

    def test_complete_inherited_superseded_and_accepted_tasks_are_exempt_from_the_edge_rule(self):
        cand, other, g = self.edge_pair()
        for status in ('complete', 'inherited', 'superseded'):
            with self.subTest(status=status):
                errors = d.validate(g, {other: status})[0]
                self.assertFalse(any(f'{other}: ' in e and 'out-of-scope task' in e for e in errors), errors)
                # the package-acceptance start rule (DLV-35) skips the same historical edge
                self.assertFalse(any(f'{other}: start prerequisite on package acceptance' in e for e in errors), errors)

        def accepted(data):
            next(x for x in data['tasks'] if x['id'] == other)['baseline'] = {'state': 'accepted', 'evidence': 'synthetic'}
        cand2, other2, g2 = self.edge_pair(accepted)
        errors = d.validate(g2)[0]  # baseline acceptance exempts the task even without a ledger record
        self.assertFalse(any(f'{other2}: ' in e and 'out-of-scope task' in e for e in errors), errors)

    def test_a_cycle_through_a_historical_edge_to_an_out_of_scope_task_is_not_a_deadlock(self):
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        other = other_task(g0, cand)
        # A feeder with no existing dependency path to or from other, so the only cycle is the one the test adds.
        feeder = next(t for t in g0.tasks if t not in (cand, other) and not g0.tasks[t].get('slice')
                      and g0.tasks[t]['kind'] != 'adoption' and g0.tasks[t]['baseline']['state'] != 'accepted'
                      and other not in g0.ancestors(t) and t not in g0.ancestors(other))

        def mutate(data):
            mark_out(data, cand)
            by_id = {x['id']: x for x in data['tasks']}
            by_id[other]['start'].append({'type': 'artifact', 'task': cand, 'need': 'n', 'why': 'w'})
            by_id[cand]['start'].append({'type': 'artifact', 'task': feeder, 'need': 'n', 'why': 'w'})
            by_id[feeder]['start'].append({'type': 'artifact', 'task': other, 'need': 'n', 'why': 'w'})
        g = self.edit_graph(mutate)
        errors = d.validate(g)[0]  # open: the start edge into the out task is refused by the edge rule ...
        self.assertTrue(any(f'{other}: start edge to out-of-scope task {cand}' in e for e in errors), errors)
        self.assertFalse(any('unsatisfiable prerequisites' in e for e in errors), errors)  # ... and the out cycle never blocks
        errors = d.validate(g, {other: 'complete'})[0]  # complete: its start edge to the out task is history
        self.assertFalse(any('unsatisfiable prerequisites' in e for e in errors), errors)
        self.assertFalse(any(f'{other}: start edge to out-of-scope task' in e for e in errors), errors)

    def test_an_open_task_may_not_start_from_an_out_of_scope_adoption_entry(self):
        # The adoption entry (DLV-22) is the repository adoption task when no slice serves the task's lane. Every real
        # repository and lane has a slice, so the test removes that slice from the in-memory index and marks the
        # adoption task out; the entry rule is then the only thing that can refuse the task.
        g0 = d.Graph(self.fx.design)
        t = next(tid for tid in sorted(g0.tasks) if not g0.tasks[tid].get('slice') and g0.tasks[tid]['kind'] != 'adoption'
                 and g0.tasks[tid]['baseline']['state'] != 'accepted' and g0.repos[g0.tasks[tid]['repo']].get('adoptionTask'))
        repo, lane = g0.tasks[t]['repo'], g0.tasks[t]['lane']
        adopt = g0.repos[repo]['adoptionTask']
        self.assertNotEqual(adopt, t)
        msg = f'{t}: entry (adoption) edge to out-of-scope task {adopt}'

        g = self.edit_graph(lambda data: mark_out(data, adopt))
        g.slice_of.pop((repo, lane))
        self.assertEqual(g.entry(t), adopt)
        for statuses in ({}, {t: None}):  # open: the entry is a start edge that may not point out
            with self.subTest(statuses=statuses):
                errors = d.validate(g, statuses)[0]
                self.assertTrue(any(msg in e for e in errors), errors)
        for status in ('delivered', 'complete', 'inherited'):  # the same entry is history for these statuses
            with self.subTest(status=status):
                errors = d.validate(g, {t: status})[0]
                self.assertFalse(any(msg in e for e in errors), errors)

    def test_satisfiability_runs_on_the_in_scope_subgraph(self):
        # Out-only cycles cannot block in-scope work, so they are not a deadlock; an in-scope cycle still is.
        g0 = d.Graph(self.fx.design)
        out_a, out_b, in_a, in_b = free_tasks(g0, 4)

        def link(data, frm, to):
            next(t for t in data['tasks'] if t['id'] == frm)['start'].append(
                {'type': 'artifact', 'task': to, 'need': 'n', 'why': 'w'})

        def out_cycle(data):
            mark_out(data, out_a)
            mark_out(data, out_b)
            link(data, out_a, out_b)
            link(data, out_b, out_a)
        self.assertEqual(d.validate(self.edit_graph(out_cycle))[0], [])

        def in_cycle(data):
            mark_out(data, out_a)
            mark_out(data, out_b)
            link(data, out_a, out_b)
            link(data, out_b, out_a)
            link(data, in_a, in_b)
            link(data, in_b, in_a)
        errors = d.validate(self.edit_graph(in_cycle))[0]
        self.assertTrue(any('unsatisfiable prerequisites (deadlock) among 2 tasks' in e for e in errors), errors)

    def test_by_must_name_a_scope_decision_record_present_in_the_design(self):
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        gate = g0.data['gates'][0]['gate']
        sub = g0.data['substitutes'][0]['id']
        # a made-up record, and a real decision that is not a scope record
        for by in ('P9-999', 'P2-021'):
            with self.subTest(by=by):
                def mutate(data, by=by):
                    mark_out(data, cand, by=by)
                    next(x for x in data['gates'] if x['gate'] == gate)['outOfScope'] = {'by': by, 'note': 'x'}
                    next(x for x in data['substitutes'] if x['id'] == sub)['outOfScope'] = {'by': by, 'note': 'x'}
                errors = d.validate(self.edit_graph(mutate))[0]
                self.assertTrue(any(f'{cand}: outOfScope names {by}, which is not a scope decision record' in e
                                    for e in errors), errors)
                self.assertTrue(any(e.startswith('outOfScopeObligations ') and f'names {by}' in e for e in errors), errors)
                self.assertTrue(any(f'gate {gate}: outOfScope names {by}' in e for e in errors), errors)
                self.assertTrue(any(f'{sub}: outOfScope names {by}' in e for e in errors), errors)

        # The reviewer's case: a marker naming an unknown record must fail check, not pass with a count.
        self.assertEqual(d.validate(self.edit_graph(lambda data: mark_out(data, cand)))[0], [])
        self.edit_graph(lambda data: mark_out(data, cand, by='P9-999'))
        code, out = self.fx.run('check')
        self.assertNotEqual(code, 0, out)
        self.assertIn(f'{cand}: outOfScope names P9-999', out)
        # The record must be present in the Design checkout that check reads (DLV-43).
        self.edit_graph(lambda data: mark_out(data, cand))
        (self.fx.design / 'docs' / 'decisions' / 'scope-record-fixture.md').unlink()
        errors = d.validate(d.Graph(self.fx.design))[0]
        self.assertTrue(any(f'{cand}: outOfScope names P2-026, which is not a scope decision record' in e
                            for e in errors), errors)

    def test_a_complete_task_is_not_blocked_by_an_out_of_scope_completion_prerequisite(self):
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        other = next(t for t in g0.tasks if t != cand and not g0.tasks[t].get('slice')
                     and g0.tasks[t]['kind'] != 'adoption' and not g0.tasks[t]['complete']
                     and g0.tasks[t]['baseline']['state'] != 'accepted')

        def mutate(data):
            mark_out(data, cand)
            next(t for t in data['tasks'] if t['id'] == other)['complete'].append(
                {'type': 'integration', 'task': cand, 'need': 'n', 'why': 'w'})
        g = self.edit_graph(mutate, commit=True)
        self.fx.record(other, 'complete')
        self.assertEqual(d.read_ledger(self.fx.plan, g)[1], [])

    def test_a_complete_task_still_needs_its_in_scope_completion_prerequisites(self):
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        other = next(t for t in g0.tasks if t != cand and not g0.tasks[t].get('slice')
                     and g0.tasks[t]['kind'] != 'adoption' and not g0.tasks[t]['complete']
                     and g0.tasks[t]['baseline']['state'] != 'accepted')
        prereq = next(t for t in g0.tasks if t not in (cand, other) and not g0.tasks[t].get('slice')
                      and g0.tasks[t]['kind'] != 'adoption')

        def mutate(data):
            mark_out(data, cand)
            next(t for t in data['tasks'] if t['id'] == other)['complete'].append(
                {'type': 'integration', 'task': prereq, 'need': 'n', 'why': 'w'})
        g = self.edit_graph(mutate, commit=True)
        self.fx.record(other, 'complete')
        errors = d.read_ledger(self.fx.plan, g)[1]
        self.assertTrue(any(f'{other} cannot be complete' in e and prereq in e for e in errors), errors)

    def test_check_refuses_a_delivered_task_whose_completion_edge_points_out_of_scope(self):
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        other = other_task(g0, cand)

        def mutate(data):
            mark_out(data, cand)
            next(t for t in data['tasks'] if t['id'] == other)['complete'].append(
                {'type': 'integration', 'task': cand, 'need': 'n', 'why': 'w'})
        self.edit_graph(mutate, commit=True)
        self.fx.record(other, 'delivered')
        self.fx.commit(self.fx.plan, 'delivered with a completion edge to an out task')
        code, out = self.fx.run('check')
        self.assertNotEqual(code, 0, out)
        self.assertIn(f'{other}: complete edge to out-of-scope task {cand}', out)

    def test_check_passes_with_historical_edges_from_a_complete_task_to_an_out_of_scope_task(self):
        self.use_full_design()
        g0 = d.Graph(self.fx.design)
        cand = pick_candidate(g0)
        other = next(t for t in g0.tasks if t != cand and not g0.tasks[t].get('slice')
                     and g0.tasks[t]['kind'] != 'adoption' and not g0.tasks[t]['complete']
                     and g0.tasks[t]['baseline']['state'] != 'accepted')

        def mutate(data):
            mark_out(data, cand)
            t = next(x for x in data['tasks'] if x['id'] == other)
            t['start'].append({'type': 'artifact', 'task': cand, 'need': 'n', 'why': 'w'})
            t['complete'].append({'type': 'integration', 'task': cand, 'need': 'n', 'why': 'w'})
        self.edit_graph(mutate, commit=True)
        self.fx.record(other, 'complete')
        self.fx.commit(self.fx.plan, 'complete with historical edges to an out task')
        self.assertEqual(self.fx.run('generate')[0], 0)
        code, out = self.fx.run('check')
        self.assertEqual(code, 0, out)

    # ---- rules E and F: analysis and generated views -------------------------------------------

    def test_schedule_measures_exclude_out_of_scope_tasks(self):
        before = d.analysis(d.Graph(self.fx.design))
        cand = pick_candidate(d.Graph(self.fx.design))
        size = d.Graph(self.fx.design).tasks[cand]['size']
        after = d.analysis(self.edit_graph(lambda data: mark_out(data, cand)))
        self.assertEqual(after['outOfScopeTasks'], 1)
        self.assertEqual(after['tasks'], before['tasks'] - 1)
        self.assertEqual(before['remainingWork'] - after['remainingWork'], d.SIZES[size])
        self.assertNotIn(cand, after['criticalPath'])
        self.assertNotIn(cand, after['initialReady'])

    def test_generate_renders_the_out_of_scope_section_and_check_passes(self):
        self.use_full_design()
        cand = pick_candidate(d.Graph(self.fx.design))
        g = self.edit_graph(lambda data: mark_out(data, cand), commit=True)
        self.fx.record(cand, 'delivered')
        self.fx.commit(self.fx.plan, 'delivered')
        code, out = self.fx.run('generate')
        self.assertEqual(code, 0, out)
        lane = g.tasks[cand]['lane']
        text = (self.fx.design / d.DELIVERY_REL / 'lanes' / f'{lane}.md').read_text(encoding='utf-8')
        head, tail = text.split('## Out of scope', 1)
        self.assertNotIn(f'\n| [{cand}](', head)  # no row in the in-scope table; Unblocks cells may still link it
        self.assertNotIn(f'<a id="{d.slug(cand)}"></a>', head)
        self.assertIn(f'<a id="{d.slug(cand)}"></a>', tail)
        self.assertIn('### P2-026', tail)
        self.assertIn('| delivered |', tail)
        self.assertIn('Out of scope (P2-026): synthetic scope test', text)
        plan_index = (self.fx.plan / 'list.md').read_text(encoding='utf-8')
        self.assertIn(cand, plan_index.split('## Out of scope', 1)[1])
        self.assertIn('1 more is out of scope under P2-026', plan_index)  # N6: singular for one task
        trace = (self.fx.design / d.DELIVERY_REL / 'traceability.md').read_text(encoding='utf-8')
        self.assertIn('Out of scope under P2-026: 1 delivery task and ', trace)
        self.assertNotIn('1 delivery tasks', trace)
        prompts = (self.fx.plan / 'tasks' / f'{lane}.md').read_text(encoding='utf-8')
        self.assertIn('### Out of scope', prompts)
        self.assertNotIn(f'Execute ArcForges delivery task {cand}', prompts)
        code, out = self.fx.run('check')
        self.assertEqual(code, 0, out)
        self.assertIn('(1 out of scope)', out)

    def test_generate_leaves_an_unscoped_graph_unchanged(self):
        self.use_full_design()
        self.assertEqual(self.fx.run('generate')[0], 0)
        self.assertEqual(sh(self.fx.design, 'status', '--porcelain'), '')


if __name__ == '__main__':
    unittest.main()
