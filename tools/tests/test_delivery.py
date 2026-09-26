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
        self.assertIn('Ready to start (68):', out)
        self.assertNotIn('ADOPT.01\t', out)

    def test_complete_ledger_requires_completed_integration_prerequisites(self):
        g = d.Graph(self.fx.design)
        self.fx.record('AND.08', 'complete')  # AND.07 is its completion prerequisite
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
        # The governance slice classifies GOV.14 as inherited: without its record the merged slice makes it ready.
        for task, status in (('ADOPT.01', 'complete'), ('ADOPT.02.governance', 'complete'), ('GOV.01', 'inherited'),
                             ('GOV.02', 'inherited'), ('GOV.03', 'inherited')):
            self.fx.record(task, status)
        self.fx.commit(self.fx.plan, 'governance slice')
        code, out = self.fx.run('ready', '--lane', 'governance')
        self.assertIn('GOV.14\tDesktopPlatform', out)
        self.fx.record('GOV.14', 'inherited')
        self.fx.commit(self.fx.plan, 'inherited record')
        code, out = self.fx.run('ready', '--lane', 'governance')
        self.assertEqual(code, 0, out)
        self.assertIn('Ready to start (1):', out)
        self.assertIn('GOV.04\tDesktopPlatform', out)
        self.assertNotIn('GOV.14\t', out)

    # ---- authoritative state and worktrees (finding 7) ----------------------------------------

    def test_unmerged_checkout_changes_never_count(self):
        self.fx.record('ADOPT.01', 'complete')
        sh(self.fx.plan, 'add', '-A')
        sh(self.fx.plan, 'commit', '--quiet', '-m', 'local only')
        code, out = self.fx.run('ready')
        self.assertIn('Ready to start (1):', out)
        code, out = self.fx.run('ready', '--local')
        self.assertIn('UNREVIEWED LOCAL STATE', out)
        self.assertIn('Ready to start (68):', out)

    def test_default_design_is_the_same_from_a_worktree(self):
        primary = self.fx.root / 'Plan-B'
        sh(self.fx.root, 'clone', '--quiet', str(self.fx.root / 'plan.git'), str(primary))
        sh(primary, 'worktree', 'add', '--quiet', '-b', 'side', str(primary / '.worktree' / 'side'))
        saved, os.environ['ARCFORGES_DESIGN'] = os.environ.get('ARCFORGES_DESIGN'), ''
        saved_root = d.PLAN_ROOT
        try:
            os.environ.pop('ARCFORGES_DESIGN')
            d.PLAN_ROOT = primary / '.worktree' / 'side'
            self.assertEqual(d.default_design().resolve(), (self.fx.root / 'ArcForges-Design-B').resolve())
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


if __name__ == '__main__':
    unittest.main()
