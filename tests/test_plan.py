"""Tests for tools/plan.py (standard library unittest)."""
import copy
import json
import hashlib
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import plan  # noqa: E402


def known_human_prerequisite():
    return sorted(plan.register_ids()[1])[0]


def pristine_graph():
    """The repository graph with every task reset to planned, for tests that change states.

    The repository graph records real delivery progress, so tests that walk a task through
    its lifecycle must not depend on the states recorded there.
    """
    g = copy.deepcopy(plan.load())
    for t in g["tasks"]:
        t["state"] = "planned"
        t["blocked_by"] = []
        t["evidence"] = {"prs": [], "merges": [], "publications": [], "ledger": None}
    return g


class GraphChecks(unittest.TestCase):
    def setUp(self):
        self.graph = plan.load()

    def test_repository_graph_is_valid(self):
        self.assertEqual(plan.validate(self.graph), [])

    def test_sequence_is_current(self):
        self.assertEqual(plan.read(plan.SEQUENCE), plan.render_sequence(self.graph))

    def test_serial_order_and_dependencies(self):
        orders = [t["order"] for t in self.graph["tasks"]]
        self.assertEqual(orders, list(range(1, len(orders) + 1)))
        g = pristine_graph()
        g["tasks"][0]["depends_on"] = [g["tasks"][5]["id"]]
        self.assertTrue(any("not earlier" in e for e in plan.validate(g)))

    def test_single_active_task(self):
        g = pristine_graph()
        g["tasks"][0]["state"] = "active"
        g["tasks"][1]["state"] = "active"
        self.assertTrue(any("more than one active" in e for e in plan.validate(g)))

    def test_delivered_needs_merge_evidence(self):
        g = pristine_graph()
        g["tasks"][0]["state"] = "delivered"
        self.assertTrue(any("without merge evidence" in e for e in plan.validate(g)))

    def test_unknown_register_entry(self):
        g = copy.deepcopy(self.graph)
        g["tasks"][0]["acceptance_register"] = ["AR-99"]
        self.assertTrue(any("AR-99" in e for e in plan.validate(g)))

    def test_missing_field(self):
        g = copy.deepcopy(self.graph)
        del g["tasks"][3]["acceptance"]
        self.assertTrue(any("missing field acceptance" in e for e in plan.validate(g)))

    def test_v2_obligations_cannot_be_omitted_or_blank(self):
        for field in ("removals", "migration", "rollback", "definition_of_done", "native_validation"):
            with self.subTest(field=field):
                g = copy.deepcopy(self.graph)
                del g["tasks"][0][field]
                self.assertTrue(any(f"missing field {field}" in e for e in plan.validate(g)))
                for blank in ("  ", [], [" "], {"linux": []}):
                    g["tasks"][0][field] = blank
                    self.assertTrue(any(f"{field} must not be empty" in e for e in plan.validate(g)))

    def test_current_graph_rejects_old_schema_and_task_namespace(self):
        g = copy.deepcopy(self.graph)
        g["schema"] = 2
        self.assertTrue(any("schema must be 3" in e for e in plan.validate(g)))
        g["schema"] = 3
        g["tasks"][0]["id"] = "AF-CTR-06"
        self.assertTrue(any("AFV2-<AREA>-<NN>" in e for e in plan.validate(g)))

    def test_native_validation_requires_both_explicit_host_arrays(self):
        g = copy.deepcopy(self.graph)
        g["tasks"][0]["native_validation"] = "run tests"
        self.assertTrue(any("native_validation must declare windows and linux arrays" in e for e in plan.validate(g)))
        g["tasks"][0]["native_validation"] = {"windows": "test Windows", "linux": ["N/A: no Linux runtime changed"]}
        self.assertTrue(any("native_validation.windows must be a nonempty array" in e for e in plan.validate(g)))

    def test_repository_and_design_paths_cannot_escape_scope(self):
        for path in ("../Cloud/**", "/etc/passwd", "C:/secrets", "src\\..\\data", ".git/config", "src//a"):
            with self.subTest(path=path):
                g = copy.deepcopy(self.graph)
                g["tasks"][0]["repositories"][0]["paths"] = [path]
                self.assertTrue(any("unsafe repository path" in e for e in plan.validate(g)))
        g = copy.deepcopy(self.graph)
        g["tasks"][0]["design_refs"] = ["../history/requirements.md"]
        self.assertTrue(any("safe current path" in e for e in plan.validate(g)))

    def test_duplicate_requirements_and_cycles_are_rejected(self):
        g = copy.deepcopy(self.graph)
        g["tasks"][0]["requirements"].append(g["tasks"][0]["requirements"][0])
        self.assertTrue(any("duplicate requirements" in e for e in plan.validate(g)))
        g = pristine_graph()
        first, second = g["tasks"][:2]
        first["depends_on"] = [second["id"]]
        second["depends_on"] = [first["id"]]
        self.assertTrue(any("dependency cycle" in e for e in plan.validate(g)))

    def test_manual_active_state_cannot_bypass_dependencies(self):
        g = pristine_graph()
        dependent = next(t for t in g["tasks"] if t["depends_on"])
        dependent["state"] = "active"
        self.assertTrue(any("dependencies not delivered or complete" in e for e in plan.validate(g)))

    def test_every_task_has_risks_covering_its_future_validation(self):
        g = copy.deepcopy(self.graph)
        g["tasks"][0]["risks"] = []
        self.assertTrue(any("risks must not be empty" in e for e in plan.validate(g)))
        g = copy.deepcopy(self.graph)
        t = next(x for x in g["tasks"] if x["future_validation"])
        f = t["future_validation"][0]
        t["risks"] = [{"risk": "something", "mitigation": "else", "owner": "user"}]
        self.assertTrue(any(f"future validation {f} is not covered" in e for e in plan.validate(g)))
        g = copy.deepcopy(self.graph)
        g["tasks"][0]["risks"][0]["owner"] = "AFV2-NOPE-99"
        self.assertTrue(any("risk owner AFV2-NOPE-99" in e for e in plan.validate(g)))

    def test_dependencies_are_real_not_a_chain(self):
        # Tasks with no real dependency exist beyond the first, so one blocked task cannot stall the plan (R-08).
        roots = [t["id"] for t in self.graph["tasks"] if not t["depends_on"]]
        self.assertGreater(len(roots), 1)

    def test_blocked_needs_register_ids(self):
        g = pristine_graph()
        g["tasks"][0]["state"] = "blocked"
        self.assertTrue(any("blocked without blocked_by" in e for e in plan.validate(g)))
        g["tasks"][0]["blocked_by"] = ["H-99"]
        self.assertTrue(any("blocked_by H-99" in e for e in plan.validate(g)))
        g["tasks"][0]["blocked_by"] = [known_human_prerequisite()]
        self.assertEqual(plan.validate(g), [])
        g["tasks"][0]["state"] = "planned"
        self.assertTrue(any("blocked_by set while" in e for e in plan.validate(g)))


class StateChanges(unittest.TestCase):
    def setUp(self):
        self.graph = pristine_graph()
        self.first = self.graph["tasks"][0]["id"]
        self.second = self.graph["tasks"][1]["id"]

    def test_next_is_first_planned(self):
        self.assertEqual(plan.next_task(self.graph)["id"], self.first)

    def test_lifecycle(self):
        plan.set_state(self.graph, self.first, "active")
        self.assertEqual(plan.next_task(self.graph)["id"], self.first)
        with self.assertRaises(SystemExit):
            plan.set_state(self.graph, self.second, "active")  # serial: one active
        with self.assertRaises(SystemExit):
            plan.set_state(self.graph, self.first, "delivered")  # needs merge evidence
        plan.set_state(self.graph, self.first, "delivered", pr="https://github.com/ArcForges/ArcForges/pull/1", merge="ArcForges@abc1234")
        self.assertEqual(plan.next_task(self.graph)["id"], self.second)
        plan.set_state(self.graph, self.first, "complete")
        with self.assertRaises(SystemExit):
            plan.set_state(self.graph, self.first, "planned")

    def test_blocked_task_is_skipped_and_does_not_count_as_active(self):
        by_id = {t["id"]: t for t in self.graph["tasks"]}
        web = next(t["id"] for t in self.graph["tasks"] if not t["depends_on"])
        with self.assertRaises(SystemExit):
            plan.set_state(self.graph, web, "blocked", reason="legal texts")  # needs --blocked-by
        with self.assertRaises(SystemExit):
            plan.set_state(self.graph, web, "planned", blocked_by=[known_human_prerequisite()])  # not a blocked transition
        plan.set_state(self.graph, web, "active")
        plan.set_state(self.graph, web, "blocked", reason="waiting for legal texts", blocked_by=[known_human_prerequisite()])
        self.assertEqual(by_id[web]["blocked_by"], [known_human_prerequisite()])
        nxt = plan.next_task(self.graph)
        self.assertNotEqual(nxt["id"], web)
        self.assertNotIn(web, nxt["depends_on"])
        plan.set_state(self.graph, nxt["id"], "active")  # allowed: the blocked task is not active
        self.assertEqual(plan.validate(self.graph), [])
        self.assertIn(f"blocked ({known_human_prerequisite()})", plan.render_sequence(self.graph))
        plan.set_state(self.graph, nxt["id"], "planned")
        plan.set_state(self.graph, web, "planned")
        self.assertEqual(by_id[web]["blocked_by"], [])

    def test_superseded_needs_reason(self):
        with self.assertRaises(SystemExit):
            plan.set_state(self.graph, self.first, "superseded")
        plan.set_state(self.graph, self.first, "superseded", reason="replaced by AD-0099")
        self.assertIn("AD-0099", self.graph["tasks"][0]["notes"])

    def test_unsatisfied_dependency_refuses_activation_without_mutating_evidence(self):
        dependent = next(t for t in self.graph["tasks"] if t["depends_on"])
        before = copy.deepcopy(self.graph)
        with self.assertRaisesRegex(SystemExit, "dependencies must be delivered or complete"):
            plan.set_state(self.graph, dependent["id"], "active", pr="https://example.invalid/attempt")
        self.assertEqual(self.graph, before)

    def test_superseded_is_not_a_delivered_dependency(self):
        first, second = self.graph["tasks"][:2]
        first["state"] = "superseded"
        second["depends_on"] = [first["id"]]
        graph = {"schema": 3, "tasks": [first, second]}
        self.assertIsNone(plan.next_task(graph))
        with self.assertRaisesRegex(SystemExit, "dependencies must be delivered or complete"):
            plan.set_state(graph, second["id"], "active")

    def test_delivery_rechecks_dependency_state(self):
        first, second = self.graph["tasks"][:2]
        first["state"] = "delivered"
        first["evidence"]["merges"] = ["ArcForges@abc1234"]
        second["depends_on"] = [first["id"]]
        plan.set_state(self.graph, second["id"], "active")
        first["state"] = "superseded"
        before = copy.deepcopy(self.graph)
        with self.assertRaisesRegex(SystemExit, "dependencies must be delivered or complete"):
            plan.set_state(self.graph, second["id"], "delivered", merge="ArcForges@def5678")
        self.assertEqual(self.graph, before)

    def test_history_graph_cannot_be_resumed(self):
        self.graph["schema"] = 2
        with self.assertRaisesRegex(SystemExit, "history is read-only"):
            plan.set_state(self.graph, self.first, "active")
        with self.assertRaisesRegex(SystemExit, "history is read-only"):
            plan.next_task(self.graph)


class EvidenceRecording(unittest.TestCase):
    def test_multi_repository_tasks_keep_every_pr_and_merge(self):
        g = pristine_graph()
        t = g["tasks"][0]
        plan.set_state(g, t["id"], "active")
        plan.set_state(g, t["id"], "delivered", pr=["https://example.invalid/a/1", "https://example.invalid/b/2"],
                       merge=["A@1111111", "B@2222222"], publication=["cohort 1"])
        self.assertEqual(t["evidence"]["prs"], ["https://example.invalid/a/1", "https://example.invalid/b/2"])
        self.assertEqual(t["evidence"]["merges"], ["A@1111111", "B@2222222"])
        self.assertEqual(t["evidence"]["publications"], ["cohort 1"])
        plan.set_state(g, t["id"], "complete", merge="A@1111111")
        self.assertEqual(t["evidence"]["merges"], ["A@1111111", "B@2222222"])


class Ledger(unittest.TestCase):
    def test_append_only_records(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ledger.jsonl"
            plan.ledger_append("AFV2-REPO-01", "started", "a", path)
            plan.ledger_append("AFV2-REPO-01", "note", "b", path)
            lines = [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines()]
            self.assertEqual([x["kind"] for x in lines], ["started", "note"])
            with self.assertRaises(SystemExit):
                plan.ledger_append("AFV2-REPO-01", "bogus", "c", path)

    def test_repository_ledger_is_valid_jsonl(self):
        for line in plan.read(plan.LEDGER).splitlines():
            rec = json.loads(line)
            self.assertIn(rec["kind"], plan.LEDGER_KINDS)

    def test_new_ledger_rejects_obsolete_task_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ledger.jsonl"
            with self.assertRaisesRegex(SystemExit, "history is read-only"):
                plan.ledger_append("AF-CTR-06", "started", "not a new task", path)
            self.assertFalse(path.exists())


class ArchiveIntegrity(unittest.TestCase):
    def make_archive(self, root):
        shutil.copytree(plan.ARCHIVE, root, dirs_exist_ok=True)
        return json.loads((root / "snapshot.json").read_text(encoding="utf-8"))

    def test_frozen_archive_matches_its_manifest(self):
        self.assertEqual(plan.validate_archive(), [])

    def test_tampered_historical_evidence_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_archive(root)
            self.assertEqual(plan.validate_archive(root), [])
            (root / "ledger/ledger.jsonl").write_bytes(b'{"kind":"complete","fake":true}\n')
            self.assertTrue(any("ledger/ledger.jsonl: SHA256 mismatch" in e for e in plan.validate_archive(root)))

    def test_archive_cannot_drop_ledger_or_escape_its_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest = self.make_archive(root)
            manifest["files"] = [manifest["files"][0], {"path": "../outside", "sha256": "0" * 64}]
            (root / "ledger/ledger.jsonl").unlink()
            (root / "snapshot.json").write_text(json.dumps(manifest), encoding="utf-8")
            errors = plan.validate_archive(root)
            self.assertTrue(any("unsafe file path" in e for e in errors))
            self.assertTrue(any("does not preserve ledger/ledger.jsonl" in e for e in errors))

    def test_file_and_manifest_cannot_be_rebaselined_together(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest = self.make_archive(root)
            ledger = root / "ledger/ledger.jsonl"
            ledger.write_bytes(ledger.read_bytes() + b'{"kind":"note","text":"rewritten evidence"}\n')
            next(entry for entry in manifest["files"] if entry["path"] == "ledger/ledger.jsonl")["sha256"] = hashlib.sha256(ledger.read_bytes()).hexdigest()
            (root / "snapshot.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
            self.assertTrue(any("manifest SHA256 differs" in e for e in plan.validate_archive(root)))

    def test_old_ids_are_allowed_only_in_history_documents(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "history").mkdir()
            (root / "history/legacy.md").write_text("AF-CTR-06 was delivered.\n", encoding="utf-8")
            (root / "README.md").write_text("Use AFV2-CENTER-01.\n", encoding="utf-8")
            self.assertEqual(plan.validate_current_documents(root), [])
            (root / "execution-prompt.md").write_text("Resume AF-CTR-06.\n", encoding="utf-8")
            self.assertTrue(any("execution-prompt.md cites obsolete task AF-CTR-06" in e
                                for e in plan.validate_current_documents(root)))


class DesignMapping(unittest.TestCase):
    def make_design(self, root):
        (root / "docs/product").mkdir(parents=True)
        (root / "docs/verification").mkdir(parents=True)
        (root / "docs/traceability").mkdir(parents=True)
        (root / "docs/product/requirements.md").write_text(
            "| R-TEST-001 | behavior | observable result | spec |\n", encoding="utf-8")
        (root / "docs/verification/platform-capabilities.md").write_text(
            "| F-MXC-01 | host behavior | AFV2-TEST-01 | NOT PROVEN |\n", encoding="utf-8")
        (root / "docs/traceability/model.json").write_text(json.dumps({"schema": 3, "requirements": [
            {"id": "R-TEST-001", "design": ["docs/product/requirements.md"], "tasks": ["AFV2-TEST-01"]}
        ]}), encoding="utf-8")
        return [{"id": "AFV2-TEST-01", "requirements": ["R-TEST-001"], "future_validation": ["F-MXC-01"],
                 "design_refs": ["docs/product/requirements.md"]}]

    def check(self, tasks, root):
        return plan.validate_design_mapping(tasks, {task["id"]: task for task in tasks}, root)

    def test_requirements_are_checked_in_both_directions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            tasks = self.make_design(root)
            self.assertEqual(self.check(tasks, root), [])
            tasks[0]["requirements"] = ["R-TEST-999"]
            errors = self.check(tasks, root)
            self.assertTrue(any("R-TEST-999 not in the design" in e for e in errors))
            self.assertTrue(any("R-TEST-001 is not covered" in e for e in errors))

    def test_duplicate_requirements_and_asymmetric_future_owner_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            tasks = self.make_design(root)
            req = root / "docs/product/requirements.md"
            req.write_text(req.read_text(encoding="utf-8") * 2, encoding="utf-8")
            tasks[0]["future_validation"] = []
            errors = self.check(tasks, root)
            self.assertTrue(any("duplicate requirement R-TEST-001" in e for e in errors))
            self.assertTrue(any("owner AFV2-TEST-01, which does not list it" in e for e in errors))

    def test_explicit_traceability_must_equal_graph_and_have_unique_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            tasks = self.make_design(root)
            model_path = root / "docs/traceability/model.json"
            model = json.loads(model_path.read_text(encoding="utf-8"))
            model["requirements"][0]["tasks"] = ["AFV2-TEST-02"]
            model["requirements"].append(copy.deepcopy(model["requirements"][0]))
            model_path.write_text(json.dumps(model), encoding="utf-8")
            errors = self.check(tasks, root)
            self.assertTrue(any("task mapping differs from graph" in e for e in errors))
            self.assertTrue(any("traceability duplicates R-TEST-001" in e for e in errors))


class RoadmapChecks(unittest.TestCase):
    """roadmap.md is the single backlog: complete rows, valid statuses, existing references (roadmap.md section 4)."""

    def setUp(self):
        self.graph = plan.load()

    def _check(self, text, graph=None):
        # Task IDs only: the repository's tasks cite real roadmap items that a minimal test roadmap lacks.
        ids_only = {"tasks": [{"id": t["id"]} for t in self.graph["tasks"]]}
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "roadmap.md"
            path.write_text(text, encoding="utf-8")
            return plan.validate_roadmap(graph or ids_only, None, path)

    def test_repository_roadmap_is_valid(self):
        self.assertEqual(plan.validate_roadmap(self.graph), [])
        ids = [rid for rid, _ in plan.roadmap_rows()]
        self.assertTrue(any(i.startswith("RM-") for i in ids))
        self.assertTrue(any(i.startswith("EX-") for i in ids))

    def test_rows_need_every_column_and_a_valid_status(self):
        task = self.graph["tasks"][0]["id"]
        good_rm = f"| RM-01 | a | b | c | d | e | f | {task} | accepted |"
        self.assertEqual(self._check(good_rm), [])
        errs = self._check("| RM-01 | a | b | c | d | e | f | AFV2-REPO-01 |")
        self.assertTrue(any("expected 9" in e for e in errs))
        errs = self._check("| RM-01 | a |  | c | d | e | f | g | accepted |")
        self.assertTrue(any("empty column" in e for e in errs))
        errs = self._check("| RM-01 | a | b | c | d | e | f | g | maybe |")
        self.assertTrue(any("invalid status" in e for e in errs))
        errs = self._check("| EX-01 | a | b | c | d | e | f | g | someday |")
        self.assertTrue(any("invalid status" in e for e in errs))
        self.assertEqual(self._check("| EX-01 | a | b | c | d | e | f | g | exploratory |"), [])
        errs = self._check("| EX-01 | a | b | c | d | exploratory |")
        self.assertTrue(any("expected 9" in e for e in errs))

    def test_malformed_ids_are_reported_not_skipped(self):
        for bad in ("RM-013", "RM-1", "rm-01", "EX-1"):
            errs = self._check(f"| {bad} | a | b | c | d | e | f | g | accepted |")
            self.assertTrue(any("malformed ID" in e for e in errs), bad)
        self.assertEqual(self._check("| ex-employee note | a |"), [])  # not an item row

    def test_references_and_duplicates(self):
        errs = self._check("| RM-01 | a | b | c | d | e | f | AFV2-NOPE-99 | accepted |")
        self.assertTrue(any("unknown task AFV2-NOPE-99" in e for e in errs))
        errs = self._check("| RM-01 | a | b | c | d | e | f | g | promoted: AFV2-NOPE-98 |")
        self.assertTrue(any("unknown task AFV2-NOPE-98" in e for e in errs))
        errs = self._check("| EX-01 | a | b | c | d | e | f | g | accepted as RM-07 |")
        self.assertTrue(any("unknown item RM-07" in e for e in errs))
        row = "| RM-01 | a | b | c | d | e | f | g | accepted |"
        errs = self._check(row + "\n" + row)
        self.assertTrue(any("duplicate RM-01" in e for e in errs))

    def test_tasks_may_cite_only_existing_items(self):
        g = copy.deepcopy(self.graph)
        g["tasks"][0]["out_of_scope"].append("Something later (roadmap RM-99)")
        self.assertTrue(any("cites RM-99" in e for e in plan.validate_roadmap(g)))


if __name__ == "__main__":
    unittest.main()
