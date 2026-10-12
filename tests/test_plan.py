"""Tests for tools/plan.py (standard library unittest)."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import plan  # noqa: E402


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
        g = copy.deepcopy(self.graph)
        g["tasks"][0]["depends_on"] = [g["tasks"][5]["id"]]
        self.assertTrue(any("not earlier" in e for e in plan.validate(g)))

    def test_single_active_task(self):
        g = copy.deepcopy(self.graph)
        g["tasks"][0]["state"] = "active"
        g["tasks"][1]["state"] = "active"
        self.assertTrue(any("more than one active" in e for e in plan.validate(g)))

    def test_delivered_needs_merge_evidence(self):
        g = copy.deepcopy(self.graph)
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


class StateChanges(unittest.TestCase):
    def setUp(self):
        self.graph = copy.deepcopy(plan.load())
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

    def test_superseded_needs_reason(self):
        with self.assertRaises(SystemExit):
            plan.set_state(self.graph, self.first, "superseded")
        plan.set_state(self.graph, self.first, "superseded", reason="replaced by AD-0099")
        self.assertIn("AD-0099", self.graph["tasks"][0]["notes"])


class Ledger(unittest.TestCase):
    def test_append_only_records(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ledger.jsonl"
            plan.ledger_append("AF-REPO-01", "started", "a", path)
            plan.ledger_append("AF-REPO-01", "note", "b", path)
            lines = [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines()]
            self.assertEqual([x["kind"] for x in lines], ["started", "note"])
            with self.assertRaises(SystemExit):
                plan.ledger_append("AF-REPO-01", "bogus", "c", path)

    def test_repository_ledger_is_valid_jsonl(self):
        for line in plan.read(plan.LEDGER).splitlines():
            rec = json.loads(line)
            self.assertIn(rec["kind"], plan.LEDGER_KINDS)


if __name__ == "__main__":
    unittest.main()
