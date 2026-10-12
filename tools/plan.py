#!/usr/bin/env python3
"""ArcForges Plan tool (serial delivery). Standard library only.

  python tools/plan.py validate [--design <ArcForges-Design root>]
  python tools/plan.py sequence [--write]
  python tools/plan.py next
  python tools/plan.py show <task-id>
  python tools/plan.py set-state <task-id> <state> [--pr URL] [--merge REPO@SHA] [--publication TEXT] [--reason TEXT]
  python tools/plan.py ledger <task-id> <kind> <text>

States: planned -> active -> delivered -> complete; any -> superseded (with --reason).
Only one task may be active at a time (execution-policy.md).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRAPH = ROOT / "delivery-graph.json"
SEQUENCE = ROOT / "sequence.md"
REGISTER = ROOT / "acceptance-register.md"
LEDGER = ROOT / "ledger" / "ledger.jsonl"

STATES = ["planned", "active", "delivered", "complete", "superseded"]
TRANSITIONS = {"planned": {"active", "superseded"}, "active": {"delivered", "planned", "superseded"},
               "delivered": {"complete", "active", "superseded"}, "complete": {"superseded"}, "superseded": set()}
REQUIRED = ["id", "title", "milestone", "order", "state", "repositories", "depends_on", "objective", "scope", "out_of_scope",
            "design_refs", "requirements", "deliverables", "acceptance", "verification", "fakes_allowed", "future_validation",
            "acceptance_register", "human_prerequisites", "risks", "size", "notes", "evidence"]
LEDGER_KINDS = {"started", "delivered", "complete", "superseded", "note", "plan"}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def load(path: Path = GRAPH) -> dict:
    return json.loads(read(path))


def save(graph: dict, path: Path = GRAPH) -> None:
    path.write_text(json.dumps(graph, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def register_ids(path: Path = REGISTER) -> tuple[set[str], set[str]]:
    text = read(path) if path.exists() else ""
    ar = set(re.findall(r"^\|\s*(AR-\d{2})\s*\|", text, re.M))
    hp = set(re.findall(r"^\|\s*(H-\d{2})\s*\|", text, re.M))
    return ar, hp


def validate(graph: dict, design: Path | None = None, register: Path = REGISTER) -> list[str]:
    errors: list[str] = []
    milestones = {m["id"] for m in graph.get("milestones", [])}
    tasks = graph.get("tasks", [])
    by_id = {}
    for t in tasks:
        tid = t.get("id", "?")
        for k in REQUIRED:
            if k not in t:
                errors.append(f"{tid}: missing field {k}")
        if tid in by_id:
            errors.append(f"duplicate task {tid}")
        by_id[tid] = t
        if not re.fullmatch(r"AF-[A-Z]+-\d{2}", tid):
            errors.append(f"{tid}: id must match AF-<AREA>-<NN>")
        if t.get("milestone") not in milestones:
            errors.append(f"{tid}: unknown milestone {t.get('milestone')}")
        if t.get("state") not in STATES:
            errors.append(f"{tid}: invalid state {t.get('state')}")
        for key in ("scope", "deliverables", "acceptance", "design_refs", "requirements", "repositories"):
            if not t.get(key):
                errors.append(f"{tid}: {key} must not be empty")
        for r in t.get("requirements", []):
            if not re.fullmatch(r"R-[A-Z]+-\d{3}", r):
                errors.append(f"{tid}: bad requirement id {r}")
        ver = t.get("verification", {})
        for k in ("author", "reviewer_distinct", "hosted_ci"):
            if not ver.get(k):
                errors.append(f"{tid}: verification.{k} must not be empty")
    orders = [t.get("order") for t in tasks]
    if orders != list(range(1, len(tasks) + 1)):
        errors.append("task order must be 1..N in file order")
    for t in tasks:
        for dep in t.get("depends_on", []):
            if dep not in by_id:
                errors.append(f"{t['id']}: unknown dependency {dep}")
            elif by_id[dep]["order"] >= t["order"]:
                errors.append(f"{t['id']}: dependency {dep} is not earlier in the serial order")
    active = [t["id"] for t in tasks if t.get("state") == "active"]
    if len(active) > 1:
        errors.append(f"more than one active task: {active}")
    ar, hp = register_ids(register)
    for t in tasks:
        for a in t.get("acceptance_register", []):
            if a not in ar:
                errors.append(f"{t['id']}: unknown acceptance-register entry {a}")
        for h in t.get("human_prerequisites", []):
            if h not in hp:
                errors.append(f"{t['id']}: unknown human prerequisite {h}")
        if t.get("state") in ("delivered", "complete") and not t["evidence"].get("merges"):
            errors.append(f"{t['id']}: {t['state']} without merge evidence")
    if design:
        req_text = read(design / "docs" / "product" / "requirements.md")
        reqs = set(re.findall(r"^\|\s*(R-[A-Z]+-\d{3})\s*\|", req_text, re.M))
        ver_text = read(design / "docs" / "verification" / "platform-capabilities.md")
        fids = set(re.findall(r"^\|\s*(F-[A-Z]\d{2})\s*\|", ver_text, re.M))
        covered = set()
        for t in tasks:
            for r in t["requirements"]:
                if r not in reqs:
                    errors.append(f"{t['id']}: requirement {r} not in the design")
                covered.add(r)
            for f in t["future_validation"]:
                if f not in fids:
                    errors.append(f"{t['id']}: future validation {f} not in the design register")
            for ref in t["design_refs"]:
                if not (design / ref).exists():
                    errors.append(f"{t['id']}: design reference {ref} does not exist")
        for r in sorted(reqs - covered):
            errors.append(f"requirement {r} is not covered by any task")
        owners = {}
        for m in re.finditer(r"^\|\s*(F-[A-Z]\d{2})\s*\|[^|]*\|\s*([^|]+)\|", ver_text, re.M):
            owners[m.group(1)] = set(re.findall(r"AF-[A-Z]+-\d{2}", m.group(2)))
        for f, own in owners.items():
            for o in own:
                if o not in by_id:
                    errors.append(f"design register {f} names unknown owner {o}")
                elif f not in by_id[o]["future_validation"]:
                    errors.append(f"design register {f} names owner {o}, which does not list it")
    return errors


def render_sequence(graph: dict) -> str:
    ms = {m["id"]: m for m in graph["milestones"]}
    out = ["# Serial delivery sequence", "",
           "Generated by `python tools/plan.py sequence --write` from [delivery-graph.json](delivery-graph.json). Do not edit by hand.",
           "Exactly one task is active at a time ([execution-policy.md](execution-policy.md)). Start the first `planned` task whose dependencies are delivered or complete (`python tools/plan.py next`).", ""]
    counts = {s: sum(1 for t in graph["tasks"] if t["state"] == s) for s in STATES}
    out.append("State: " + ", ".join(f"{s} {n}" for s, n in counts.items()) + ".")
    current = None
    for t in graph["tasks"]:
        if t["milestone"] != current:
            current = t["milestone"]
            m = ms[current]
            out += ["", f"## {m['id']} — {m['title']}", "", f"Outcome: {m['outcome']}", "",
                    "| # | Task | Title | Repositories | Depends on | Size | State |", "|---|---|---|---|---|---|---|"]
        repos = ", ".join(r["repo"] for r in t["repositories"])
        deps = ", ".join(t["depends_on"]) or "—"
        out.append(f"| {t['order']} | {t['id']} | {t['title']} | {repos} | {deps} | {t['size']} | {t['state']} |")
    return "\n".join(out) + "\n"


def next_task(graph: dict) -> dict | None:
    by_id = {t["id"]: t for t in graph["tasks"]}
    for t in graph["tasks"]:
        if t["state"] == "active":
            return t
    for t in graph["tasks"]:
        if t["state"] == "planned" and all(by_id[d]["state"] in ("delivered", "complete", "superseded") for d in t["depends_on"]):
            return t
    return None


def set_state(graph: dict, tid: str, state: str, pr=None, merge=None, publication=None, reason=None) -> None:
    by_id = {t["id"]: t for t in graph["tasks"]}
    if tid not in by_id:
        raise SystemExit(f"unknown task {tid}")
    t = by_id[tid]
    if state not in TRANSITIONS[t["state"]]:
        raise SystemExit(f"{tid}: {t['state']} -> {state} is not allowed")
    if state == "active" and any(x["state"] == "active" for x in graph["tasks"] if x["id"] != tid):
        raise SystemExit("another task is active; serial policy allows one")
    if state == "superseded" and not reason:
        raise SystemExit("superseded needs --reason")
    if state in ("delivered", "complete") and not (merge or t["evidence"]["merges"]):
        raise SystemExit(f"{state} needs --merge evidence")
    if pr:
        t["evidence"]["prs"].append(pr)
    if merge:
        t["evidence"]["merges"].append(merge)
    if publication:
        t["evidence"]["publications"].append(publication)
    if reason:
        t["notes"] = (t["notes"] + " " if t["notes"] else "") + f"[{state}] {reason}"
    t["state"] = state


def ledger_append(tid: str, kind: str, text: str, path: Path = LEDGER) -> dict:
    if kind not in LEDGER_KINDS:
        raise SystemExit(f"kind must be one of {sorted(LEDGER_KINDS)}")
    rec = {"at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "task": tid, "kind": kind, "text": text}
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="plan.py")
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate")
    v.add_argument("--design", type=Path)
    s = sub.add_parser("sequence")
    s.add_argument("--write", action="store_true")
    sub.add_parser("next")
    sh = sub.add_parser("show")
    sh.add_argument("task")
    ss = sub.add_parser("set-state")
    ss.add_argument("task")
    ss.add_argument("state", choices=STATES)
    ss.add_argument("--pr")
    ss.add_argument("--merge")
    ss.add_argument("--publication")
    ss.add_argument("--reason")
    lg = sub.add_parser("ledger")
    lg.add_argument("task")
    lg.add_argument("kind")
    lg.add_argument("text")
    args = ap.parse_args(argv)
    graph = load()
    if args.cmd == "validate":
        errs = validate(graph, args.design)
        rendered = render_sequence(graph)
        if not SEQUENCE.exists() or read(SEQUENCE) != rendered:
            errs.append("sequence.md is out of date (run: python tools/plan.py sequence --write)")
        for e in errs:
            print(f"ERROR: {e}")
        print(f"{len(errs)} error(s); {len(graph['tasks'])} tasks, {len(graph['milestones'])} milestones")
        return 1 if errs else 0
    if args.cmd == "sequence":
        text = render_sequence(graph)
        if args.write:
            SEQUENCE.write_text(text, encoding="utf-8", newline="\n")
        else:
            print(text)
        return 0
    if args.cmd == "next":
        t = next_task(graph)
        print(json.dumps({"id": t["id"], "title": t["title"], "state": t["state"]} if t else None))
        return 0
    if args.cmd == "show":
        t = next((x for x in graph["tasks"] if x["id"] == args.task), None)
        if t is None:
            print(f"unknown task {args.task}")
            return 1
        print(json.dumps(t, indent=2, ensure_ascii=False))
        return 0
    if args.cmd == "set-state":
        set_state(graph, args.task, args.state, args.pr, args.merge, args.publication, args.reason)
        save(graph)
        SEQUENCE.write_text(render_sequence(graph), encoding="utf-8", newline="\n")
        print(f"{args.task} -> {args.state}")
        return 0
    if args.cmd == "ledger":
        print(json.dumps(ledger_append(args.task, args.kind, args.text)))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
