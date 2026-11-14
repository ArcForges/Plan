#!/usr/bin/env python3
"""ArcForges Plan tool (serial delivery). Standard library only.

  python tools/plan.py validate [--design <ArcForges-Design root>]
  python tools/plan.py sequence [--write]
  python tools/plan.py next
  python tools/plan.py show <task-id>
  python tools/plan.py set-state <task-id> <state> [--pr URL] [--merge REPO@SHA] [--publication TEXT] [--reason TEXT] [--blocked-by H-xx,AR-yy]
  python tools/plan.py ledger <task-id> <kind> <text>

States: planned -> active -> delivered -> complete; any -> superseded (with --reason).
A planned or active task waiting on a human prerequisite or register entry becomes `blocked`
(with --blocked-by and --reason). `next` skips blocked tasks and their dependents, and a blocked task
does not count against the single active task (execution-policy.md section 2).
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
GRAPH = ROOT / "delivery-graph.json"
SEQUENCE = ROOT / "sequence.md"
REGISTER = ROOT / "acceptance-register.md"
ROADMAP = ROOT / "roadmap.md"
LEDGER = ROOT / "ledger" / "ledger.jsonl"
ARCHIVE = ROOT / "history" / "v1-20261114"
ARCHIVE_COMMIT = "742ed2660c5e934e1df86f90e54198b3a199e2b1"
ARCHIVE_MANIFEST_SHA256 = "6cbac6eec1f98f76ecbdd83a5df50f47cf2127998680f46d7a44928473b935f3"

TASK_PATTERN = r"AFV2-[A-Z]+-\d{2}"
TASK_ID = re.compile(TASK_PATTERN)
TASK_REF = re.compile(rf"\b{TASK_PATTERN}\b")
OLD_TASK_REF = re.compile(r"\bAF-[A-Z]+-\d{2}\b")
REQUIREMENT_PATTERN = r"R-[A-Z]+-\d{3}"
FUTURE_PATTERN = r"F-[A-Z]+-\d{2}"
READY_STATES = {"delivered", "complete"}

STATES = ["planned", "active", "blocked", "delivered", "complete", "superseded"]
TRANSITIONS = {"planned": {"active", "blocked", "superseded"}, "active": {"delivered", "planned", "blocked", "superseded"},
               "blocked": {"planned", "active", "superseded"},
               "delivered": {"complete", "active", "superseded"}, "complete": {"superseded"}, "superseded": set()}
REQUIRED = ["id", "title", "milestone", "order", "state", "repositories", "depends_on", "objective", "scope", "out_of_scope",
            "design_refs", "requirements", "deliverables", "acceptance", "verification", "fakes_allowed", "future_validation",
            "acceptance_register", "human_prerequisites", "risks", "size", "notes", "blocked_by", "evidence",
            "removals", "migration", "rollback", "definition_of_done", "native_validation"]
LEDGER_KINDS = {"started", "delivered", "complete", "superseded", "note", "plan"}
# roadmap.md tables: RM rows have 9 columns (ID, Item, Purpose, Why deferred, Prerequisites, Revisit when,
# Foundations in release 1, References, Status); EX rows have 9 (ID, Idea, Purpose, Why not now,
# Prerequisites, Question to answer, Revisit when, References, Status).
RM_COLUMNS = 9
EX_COLUMNS = 9
RM_STATUS = re.compile(rf"accepted|promoted: {TASK_PATTERN}(, {TASK_PATTERN})*|dropped: .+")
EX_STATUS = re.compile(r"exploratory|accepted as RM-\d{2}|dropped: .+")
ROADMAP_REF = re.compile(r"\b(?:RM|EX)-\d{2}\b")


def nonempty(value) -> bool:
    """Structured task obligations must contain actual content, not blank shells."""
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return bool(value) and all(nonempty(item) for item in value)
    if isinstance(value, dict):
        return bool(value) and all(isinstance(key, str) and key.strip() and nonempty(item)
                                   for key, item in value.items())
    return False


def safe_relative_path(value: object, *, globs: bool = False) -> bool:
    """Repository paths use portable slash-separated relative paths/globs."""
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        return False
    if any(ord(c) < 32 for c in value) or any(c in value for c in "\\:~"):
        return False
    if value.startswith("/") or any(part in ("", ".", "..", ".git", ".worktree") for part in value.split("/")):
        return False
    if not globs and any(c in value for c in "*?[]"):
        return False
    return not PurePosixPath(value).is_absolute()


def validate_archive(path: Path = ARCHIVE) -> list[str]:
    """Frozen evidence is checked as bytes and is never loaded as active tasks."""
    manifest_path = path / "snapshot.json"
    errors = []
    try:
        if hashlib.sha256(manifest_path.read_bytes()).hexdigest() != ARCHIVE_MANIFEST_SHA256:
            errors.append("archive snapshot manifest SHA256 differs from its frozen identity; rebaselining is forbidden")
        manifest = load(manifest_path)
    except (OSError, ValueError) as exc:
        return errors + [f"archive snapshot cannot be read: {exc}"]
    if manifest.get("source_repository") != "ArcForges/Plan" or manifest.get("source_commit") != ARCHIVE_COMMIT:
        errors.append("archive snapshot source identity differs from the frozen Plan baseline")
    entries = manifest.get("files")
    if not isinstance(entries, list) or not entries:
        return errors + ["archive snapshot files must be a nonempty list"]
    listed = set()
    for entry in entries:
        if not isinstance(entry, dict) or not safe_relative_path(entry.get("path")):
            errors.append("archive snapshot contains an unsafe file path")
            continue
        name = entry["path"]
        if name in listed:
            errors.append(f"archive snapshot duplicates {name}")
        listed.add(name)
        expected = entry.get("sha256", "")
        if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
            errors.append(f"archive {name}: invalid SHA256")
            continue
        file = path / name
        if not file.is_file() or file.is_symlink() or not file.resolve().is_relative_to(path.resolve()):
            errors.append(f"archive {name}: missing or unsafe file")
            continue
        if hashlib.sha256(file.read_bytes()).hexdigest() != expected:
            errors.append(f"archive {name}: SHA256 mismatch")
    for required in ("delivery-graph.json", "ledger/ledger.jsonl"):
        if required not in listed:
            errors.append(f"archive snapshot does not preserve {required}")
    actual = {p.relative_to(path).as_posix() for p in path.rglob("*") if p.is_file()} - {"snapshot.json"}
    for name in sorted(actual - listed):
        errors.append(f"archive {name}: file is not in the frozen snapshot")
    return errors


def validate_current_documents(root: Path = ROOT) -> list[str]:
    """Execution documents may link history, but may not name old executable tasks."""
    errors = []
    paths = sorted(root.glob("*.md")) + [root / "ledger/README.md"]
    for path in paths:
        if path.is_file():
            for tid in sorted(set(OLD_TASK_REF.findall(read(path)))):
                errors.append(f"current {path.relative_to(root).as_posix()} cites obsolete task {tid}; use the frozen history")
    return errors


def validate_ledger(graph: dict, path: Path = LEDGER) -> list[str]:
    if not path.is_file():
        return ["current ledger is missing"]
    errors = []
    known = {task.get("id") for task in graph.get("tasks", []) if isinstance(task.get("id"), str)}
    for number, line in enumerate(read(path).splitlines(), 1):
        try:
            record = json.loads(line)
        except ValueError:
            errors.append(f"current ledger line {number}: invalid JSON")
            continue
        if not isinstance(record, dict) or not isinstance(record.get("kind"), str) or record["kind"] not in LEDGER_KINDS:
            errors.append(f"current ledger line {number}: invalid record kind")
            continue
        tid = record.get("task")
        if tid != "PLAN" and (not isinstance(tid, str) or not TASK_ID.fullmatch(tid) or tid not in known):
            errors.append(f"current ledger line {number}: unknown or obsolete task {tid}")
        if not isinstance(record.get("at"), str) or not nonempty(record.get("text")):
            errors.append(f"current ledger line {number}: timestamp and text are required")
    return errors


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def load(path: Path = GRAPH) -> dict:
    value = json.loads(read(path))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def save(graph: dict, path: Path = GRAPH) -> None:
    path.write_text(json.dumps(graph, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def register_ids(path: Path = REGISTER) -> tuple[set[str], set[str]]:
    text = read(path) if path.exists() else ""
    ar = set(re.findall(r"^\|\s*(AR-\d{2})\s*\|", text, re.M))
    hp = set(re.findall(r"^\|\s*(H-\d{2})\s*\|", text, re.M))
    return ar, hp


def roadmap_rows(path: Path = ROADMAP) -> list[tuple[str, list[str]]]:
    """Rows of the roadmap tables in file order: (ID, cells) for RM-xx and EX-xx rows."""
    rows: list[tuple[str, list[str]]] = []
    if not path.exists():
        return rows
    for line in read(path).split("\n"):
        m = re.match(r"^\|\s*([^|]*?)\s*\|", line)
        if m and re.match(r"(?i)(rm|ex)-\d", m.group(1)):
            rows.append((m.group(1), [c.strip() for c in line.strip().strip("|").split("|")]))
    return rows


def validate_roadmap(graph: dict, design: Path | None = None, path: Path = ROADMAP) -> list[str]:
    """roadmap.md is the only backlog (its section 4): complete rows, valid statuses, existing references."""
    if not path.exists():
        return ["roadmap.md is missing"]
    errors: list[str] = []
    rows = roadmap_rows(path)
    ids = [rid for rid, _ in rows]
    for rid in sorted({i for i in ids if ids.count(i) > 1}):
        errors.append(f"roadmap: duplicate {rid}")
    known = set(ids)
    tasks = {t["id"] for t in graph.get("tasks", [])}
    reqs: set[str] | None = None
    adrs: set[str] | None = None
    if design:
        req_path = design / "docs" / "product" / "requirements.md"
        if not req_path.is_file():
            errors.append("design requirements are missing")
        reqs = set(re.findall(r"^\|\s*(R-[A-Z]+-\d{3})\s*\|", read(req_path), re.M)) if req_path.is_file() else set()
        adrs = {p.name[:7] for p in (design / "docs" / "decisions").glob("AD-*.md")}
    for rid, cells in rows:
        if not re.fullmatch(r"(RM|EX)-\d{2}", rid):
            errors.append(f"roadmap: malformed ID {rid!r} (expected RM-NN or EX-NN)")
            continue
        want = RM_COLUMNS if rid.startswith("RM") else EX_COLUMNS
        if len(cells) != want:
            errors.append(f"roadmap: {rid} has {len(cells)} columns, expected {want}")
            continue
        if any(not c for c in cells):
            errors.append(f"roadmap: {rid} has an empty column")
        status = cells[-1]
        if not (RM_STATUS if rid.startswith("RM") else EX_STATUS).fullmatch(status):
            errors.append(f"roadmap: {rid} has an invalid status {status!r}")
        text = " ".join(cells)
        for tid in sorted(set(TASK_REF.findall(text)) - tasks):
            errors.append(f"roadmap: {rid} names unknown task {tid}")
        for tid in sorted(set(OLD_TASK_REF.findall(text))):
            errors.append(f"roadmap: {rid} cites obsolete task {tid}; use the frozen history")
        for ref in sorted(set(re.findall(r"\bRM-\d{2}\b", status)) - known):
            errors.append(f"roadmap: {rid} names unknown item {ref}")
        if reqs is not None:
            for r in sorted(set(re.findall(r"\bR-[A-Z]+-\d{3}\b", text)) - reqs):
                errors.append(f"roadmap: {rid} names unknown requirement {r}")
        if adrs is not None:
            for a in sorted(set(re.findall(r"\bAD-\d{4}\b", text)) - adrs):
                errors.append(f"roadmap: {rid} names unknown decision {a}")
    for t in graph.get("tasks", []):
        for ref in sorted(set(ROADMAP_REF.findall(json.dumps(t, ensure_ascii=False))) - known):
            errors.append(f"{t['id']}: cites {ref}, which is not in roadmap.md")
    if design:
        cited: dict[str, str] = {}
        for p in sorted((design / "docs").rglob("*")):
            if p.is_file() and p.suffix in (".md", ".proto", ".json", ".sql"):
                for ref in ROADMAP_REF.findall(read(p)):
                    cited.setdefault(ref, p.relative_to(design).as_posix())
        for ref, where in sorted(cited.items()):
            if ref not in known:
                errors.append(f"design {where} cites {ref}, which is not in roadmap.md")
    return errors


def dependencies_ready(task: dict, by_id: dict[str, dict]) -> bool:
    return all(isinstance(dep, str) and dep in by_id and isinstance(by_id[dep].get("state"), str)
               and by_id[dep]["state"] in READY_STATES
               for dep in task.get("depends_on", []))


def validate(graph: dict, design: Path | None = None, register: Path = REGISTER, roadmap: Path = ROADMAP,
             archive: Path = ARCHIVE, current_root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    if type(graph.get("schema")) is not int or graph["schema"] != 3:
        errors.append("current graph schema must be 3; historical graphs are not executable")
    milestone_rows = graph.get("milestones", [])
    if not isinstance(milestone_rows, list) or not all(isinstance(m, dict) for m in milestone_rows):
        return errors + ["milestones must be a list of objects"]
    milestone_ids = [m.get("id") for m in milestone_rows]
    if any(not isinstance(mid, str) or not mid.strip() for mid in milestone_ids):
        errors.append("milestones need nonempty string IDs")
    if len(milestone_ids) != len(set(str(mid) for mid in milestone_ids)):
        errors.append("duplicate milestone ID")
    milestones = {mid for mid in milestone_ids if isinstance(mid, str)}
    tasks = graph.get("tasks", [])
    if not isinstance(tasks, list) or not tasks or not all(isinstance(t, dict) for t in tasks):
        return errors + ["tasks must be a nonempty list of objects"]
    by_id = {}
    list_fields = ("repositories", "depends_on", "scope", "out_of_scope", "design_refs", "requirements", "deliverables",
                   "acceptance", "fakes_allowed", "future_validation", "acceptance_register", "human_prerequisites",
                   "risks", "blocked_by")
    for t in tasks:
        tid = t.get("id", "?")
        for key in REQUIRED:
            if key not in t:
                errors.append(f"{tid}: missing field {key}")
        if not isinstance(tid, str) or not TASK_ID.fullmatch(tid):
            errors.append(f"{tid}: id must match AFV2-<AREA>-<NN>")
        if isinstance(tid, str):
            if tid in by_id:
                errors.append(f"duplicate task {tid}")
            by_id[tid] = t
        for key in list_fields:
            if key in t and not isinstance(t[key], list):
                errors.append(f"{tid}: {key} must be a list")
        if any(key in t and not isinstance(t[key], list) for key in list_fields):
            continue
        if not isinstance(t.get("milestone"), str) or t["milestone"] not in milestones:
            errors.append(f"{tid}: unknown milestone {t.get('milestone')}")
        if t.get("state") not in STATES:
            errors.append(f"{tid}: invalid state {t.get('state')}")
        for key in ("title", "objective", "scope", "deliverables", "acceptance", "design_refs", "requirements",
                    "repositories", "removals", "migration", "rollback", "definition_of_done", "native_validation"):
            if not nonempty(t.get(key)):
                errors.append(f"{tid}: {key} must not be empty")
        native = t.get("native_validation")
        if not isinstance(native, dict) or set(native) != {"windows", "linux"}:
            errors.append(f"{tid}: native_validation must declare windows and linux arrays")
        else:
            for host in ("windows", "linux"):
                if not isinstance(native[host], list) or not native[host] or not all(isinstance(step, str) and step.strip() for step in native[host]):
                    errors.append(f"{tid}: native_validation.{host} must be a nonempty array of validation steps or an explicit N/A reason")
        for key, pattern in (("requirements", REQUIREMENT_PATTERN), ("future_validation", FUTURE_PATTERN),
                             ("depends_on", TASK_PATTERN)):
            values = t.get(key, [])
            for value in values:
                if not isinstance(value, str) or not re.fullmatch(pattern, value):
                    errors.append(f"{tid}: bad {key} id {value}")
            if len(values) != len(set(str(value) for value in values)):
                errors.append(f"{tid}: duplicate {key} entry")
        repo_names = set()
        for repo in t.get("repositories", []):
            if not isinstance(repo, dict) or not isinstance(repo.get("repo"), str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]*", repo["repo"]):
                errors.append(f"{tid}: repository scope needs a safe repository name")
                continue
            if repo["repo"] in repo_names:
                errors.append(f"{tid}: duplicate repository scope {repo['repo']}")
            repo_names.add(repo["repo"])
            paths = repo.get("paths")
            if not isinstance(paths, list) or not paths:
                errors.append(f"{tid}: {repo['repo']} paths must be a nonempty list")
                continue
            for path in paths:
                if not safe_relative_path(path, globs=True):
                    errors.append(f"{tid}: unsafe repository path {path!r}")
        for ref in t.get("design_refs", []):
            if not safe_relative_path(ref) or str(ref).startswith("history/"):
                errors.append(f"{tid}: design reference must be a safe current path: {ref!r}")
        ver = t.get("verification", {})
        for key in ("author", "reviewer_distinct", "hosted_ci"):
            if not isinstance(ver, dict) or not nonempty(ver.get(key)):
                errors.append(f"{tid}: verification.{key} must not be empty")
        evidence = t.get("evidence", {})
        if not isinstance(evidence, dict) or any(not isinstance(evidence.get(key), list) for key in ("prs", "merges", "publications")):
            errors.append(f"{tid}: evidence needs prs, merges and publications lists")
        risks = t.get("risks") or []
        if not risks:
            errors.append(f"{tid}: risks must not be empty")
        risk_text = ""
        for risk in risks:
            if not isinstance(risk, dict) or not all(nonempty(risk.get(key)) for key in ("risk", "mitigation", "owner")):
                errors.append(f"{tid}: each risk needs risk, mitigation and owner")
                continue
            risk_text += f" {risk['risk']} {risk['mitigation']}"
        for future in t.get("future_validation", []):
            if isinstance(future, str) and future not in risk_text:
                errors.append(f"{tid}: future validation {future} is not covered by a risk")
    # Type errors have already been reported; do not crash while following lists.
    if any(key in t and not isinstance(t[key], list) for t in tasks for key in list_fields):
        return errors
    for t in tasks:
        for key in ("depends_on", "requirements", "future_validation", "acceptance_register", "human_prerequisites", "blocked_by", "design_refs"):
            if any(not isinstance(value, str) for value in t.get(key, [])):
                return errors + [f"{t.get('id', '?')}: {key} entries must be strings"]
    orders = [t.get("order") for t in tasks]
    if any(type(order) is not int for order in orders) or orders != list(range(1, len(tasks) + 1)):
        errors.append("task order must be 1..N in file order")
    for t in tasks:
        tid = t.get("id", "?")
        for risk in t.get("risks") or []:
            owner = risk.get("owner") if isinstance(risk, dict) else None
            if isinstance(owner, str) and owner != "user" and owner not in by_id:
                errors.append(f"{tid}: risk owner {owner} is not a task or 'user'")
        for dep in t.get("depends_on", []):
            if not isinstance(dep, str) or dep not in by_id:
                errors.append(f"{tid}: unknown dependency {dep}")
            elif type(by_id[dep].get("order")) is int and type(t.get("order")) is int and by_id[dep]["order"] >= t["order"]:
                errors.append(f"{tid}: dependency {dep} is not earlier in the serial order")
        if isinstance(t.get("state"), str) and t["state"] in READY_STATES | {"active"} and not dependencies_ready(t, by_id):
            errors.append(f"{tid}: {t['state']} with dependencies not delivered or complete")
    visiting, visited = set(), set()

    def visit(tid):
        if tid in visiting:
            errors.append(f"dependency cycle includes {tid}")
            return
        if tid in visited:
            return
        visiting.add(tid)
        for dep in by_id[tid].get("depends_on", []):
            if isinstance(dep, str) and dep in by_id:
                visit(dep)
        visiting.remove(tid)
        visited.add(tid)

    for tid in by_id:
        visit(tid)
    active = [t.get("id") for t in tasks if t.get("state") == "active"]
    if len(active) > 1:
        errors.append(f"more than one active task: {active}")
    ar, hp = register_ids(register)
    for t in tasks:
        tid = t.get("id", "?")
        for entry in t.get("acceptance_register", []):
            if entry not in ar:
                errors.append(f"{tid}: unknown acceptance-register entry {entry}")
        for entry in t.get("human_prerequisites", []):
            if entry not in hp:
                errors.append(f"{tid}: unknown human prerequisite {entry}")
        evidence = t.get("evidence")
        if isinstance(t.get("state"), str) and t["state"] in READY_STATES and (not isinstance(evidence, dict) or not evidence.get("merges")):
            errors.append(f"{tid}: {t['state']} without merge evidence")
        blocked_by = t.get("blocked_by") or []
        if t.get("state") == "blocked":
            if not blocked_by:
                errors.append(f"{tid}: blocked without blocked_by")
            for entry in blocked_by:
                if entry not in ar and entry not in hp:
                    errors.append(f"{tid}: blocked_by {entry} is not in the acceptance register")
        elif blocked_by:
            errors.append(f"{tid}: blocked_by set while the state is {t.get('state')}")
    if design:
        errors += validate_design_mapping(tasks, by_id, design)
    errors += validate_roadmap(graph, design, roadmap)
    errors += validate_archive(archive)
    errors += validate_current_documents(current_root)
    errors += validate_ledger(graph, current_root / "ledger/ledger.jsonl")
    return errors


def validate_design_mapping(tasks: list[dict], by_id: dict[str, dict], design: Path) -> list[str]:
    errors = []
    requirements = design / "docs/product/requirements.md"
    capabilities = design / "docs/verification/platform-capabilities.md"
    if not requirements.is_file() or not capabilities.is_file():
        return ["design requirements or platform-capabilities register is missing"]
    req_rows = re.findall(rf"^\|\s*({REQUIREMENT_PATTERN})\s*\|", read(requirements), re.M)
    reqs = set(req_rows)
    if not reqs:
        errors.append("design has no current requirement rows")
    for req in sorted(reqs):
        if req_rows.count(req) > 1:
            errors.append(f"design has duplicate requirement {req}")
    future_rows = []
    for line in read(capabilities).splitlines():
        match = re.match(rf"^\|\s*({FUTURE_PATTERN})\s*\|", line)
        if match:
            future_rows.append((match[1], set(TASK_REF.findall(line))))
    futures = {fid for fid, _ in future_rows}
    owners = {}
    for fid, current_owners in future_rows:
        if fid in owners:
            errors.append(f"design register duplicates {fid}")
        owners[fid] = current_owners
        if not current_owners:
            errors.append(f"design register {fid} has no task owner")
    covered = set()
    for t in tasks:
        tid = t.get("id", "?")
        for req in t.get("requirements", []):
            if isinstance(req, str):
                if req not in reqs:
                    errors.append(f"{tid}: requirement {req} not in the design")
                covered.add(req)
        for future in t.get("future_validation", []):
            if future not in futures:
                errors.append(f"{tid}: future validation {future} not in the design register")
            elif tid not in owners[future]:
                errors.append(f"{tid}: design register {future} does not name it as an owner")
        for ref in t.get("design_refs", []):
            if safe_relative_path(ref) and not (design / ref).is_file():
                errors.append(f"{tid}: design reference {ref} does not exist")
    for req in sorted(reqs - covered):
        errors.append(f"requirement {req} is not covered by any task")
    for fid, current_owners in owners.items():
        for owner in current_owners:
            if owner not in by_id:
                errors.append(f"design register {fid} names unknown owner {owner}")
            elif fid not in by_id[owner].get("future_validation", []):
                errors.append(f"design register {fid} names owner {owner}, which does not list it")
    model_path = design / "docs/traceability/model.json"
    try:
        model = load(model_path)
    except (OSError, ValueError) as exc:
        return errors + [f"design traceability model cannot be read: {exc}"]
    if not isinstance(model, dict) or type(model.get("schema")) is not int or model["schema"] != 3:
        return errors + ["design traceability model schema must be 3"]
    mappings = model.get("requirements")
    if not isinstance(mappings, list) or not mappings:
        return errors + ["design traceability requirements must be a nonempty list"]
    mapped = set()
    for entry in mappings:
        if not isinstance(entry, dict) or not isinstance(entry.get("id"), str) or not re.fullmatch(REQUIREMENT_PATTERN, entry["id"]):
            errors.append("design traceability has a malformed requirement entry")
            continue
        req = entry["id"]
        if req in mapped:
            errors.append(f"design traceability duplicates {req}")
        mapped.add(req)
        if req not in reqs:
            errors.append(f"design traceability {req} is not a current requirement")
        task_ids = entry.get("tasks")
        if not isinstance(task_ids, list) or not task_ids or not all(isinstance(tid, str) and TASK_ID.fullmatch(tid) for tid in task_ids):
            errors.append(f"design traceability {req} needs current task IDs")
        else:
            if len(task_ids) != len(set(task_ids)):
                errors.append(f"design traceability {req} has duplicate tasks")
            actual = {t.get("id") for t in tasks if req in t.get("requirements", [])}
            if set(task_ids) != actual:
                errors.append(f"design traceability {req} task mapping differs from graph: design={sorted(set(task_ids))}, graph={sorted(actual)}")
        paths = entry.get("design")
        if not isinstance(paths, list) or not paths:
            errors.append(f"design traceability {req} needs nonempty design paths")
        else:
            for path in paths:
                if not safe_relative_path(path) or path.startswith("history/") or not (design / path).is_file():
                    errors.append(f"design traceability {req} has an unsafe or missing current design path {path!r}")
            if len(paths) != len(set(str(path) for path in paths)):
                errors.append(f"design traceability {req} has duplicate design paths")
    for req in sorted(reqs - mapped):
        errors.append(f"design traceability is missing requirement {req}")
    return errors


def render_sequence(graph: dict) -> str:
    ms = {m["id"]: m for m in graph["milestones"]}
    out = ["# Serial delivery sequence", "",
           "Generated by `python tools/plan.py sequence --write` from [delivery-graph.json](delivery-graph.json). Do not edit by hand.",
           "Exactly one task is active at a time ([execution-policy.md](execution-policy.md)). Work is authorized per range of rows of this table ([execution-prompt.md](execution-prompt.md)); within a range, start the first `planned` task whose dependencies are delivered or complete.",
           "`Depends on` lists only real dependencies; the row order is the serial sequence. A `blocked` task waits on the named register entries, and `next` continues with tasks that do not depend on it.", ""]
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
        state = t["state"] + (f" ({', '.join(t['blocked_by'])})" if t["state"] == "blocked" else "")
        out.append(f"| {t['order']} | {t['id']} | {t['title']} | {repos} | {deps} | {t['size']} | {state} |")
    return "\n".join(out) + "\n"


def next_task(graph: dict) -> dict | None:
    if graph.get("schema") != 3:
        raise SystemExit("next requires the current schema-3 graph; history is read-only")
    by_id = {t["id"]: t for t in graph["tasks"]}
    for t in graph["tasks"]:
        if t["state"] == "active":
            if not dependencies_ready(t, by_id):
                raise SystemExit(f"{t['id']}: active task has dependencies not delivered or complete")
            return t
    for t in graph["tasks"]:
        if t["state"] == "planned" and dependencies_ready(t, by_id):
            return t
    return None


def set_state(graph: dict, tid: str, state: str, pr=None, merge=None, publication=None, reason=None, blocked_by=None) -> None:
    if graph.get("schema") != 3 or not TASK_ID.fullmatch(tid):
        raise SystemExit("state changes require a current schema-3 AFV2 task; history is read-only")
    by_id = {t["id"]: t for t in graph["tasks"]}
    if tid not in by_id:
        raise SystemExit(f"unknown task {tid}")
    t = by_id[tid]
    if state not in TRANSITIONS[t["state"]]:
        raise SystemExit(f"{tid}: {t['state']} -> {state} is not allowed")
    if state == "active" and any(x["state"] == "active" for x in graph["tasks"] if x["id"] != tid):
        raise SystemExit("another task is active; serial policy allows one")
    if state in READY_STATES | {"active"} and not dependencies_ready(t, by_id):
        pending = [dep for dep in t["depends_on"] if dep not in by_id or by_id[dep]["state"] not in READY_STATES]
        raise SystemExit(f"{tid}: dependencies must be delivered or complete: {', '.join(pending)}")
    if state == "superseded" and not reason:
        raise SystemExit("superseded needs --reason")
    if state == "blocked" and not (blocked_by and reason):
        raise SystemExit("blocked needs --blocked-by and --reason")
    if state != "blocked" and blocked_by:
        raise SystemExit("--blocked-by applies only to the blocked state")
    if state in ("delivered", "complete") and not (merge or t["evidence"]["merges"]):
        raise SystemExit(f"{state} needs --merge evidence")
    # Each option may be given once per repository (a task can span several repositories).
    for key, values in (("prs", pr), ("merges", merge), ("publications", publication)):
        for v in ([values] if isinstance(values, str) else (values or [])):
            if v not in t["evidence"][key]:
                t["evidence"][key].append(v)
    if reason:
        t["notes"] = (t["notes"] + " " if t["notes"] else "") + f"[{state}] {reason}"
    t["blocked_by"] = list(blocked_by) if state == "blocked" else []
    t["state"] = state


def ledger_append(tid: str, kind: str, text: str, path: Path = LEDGER) -> dict:
    if tid != "PLAN" and not TASK_ID.fullmatch(tid):
        raise SystemExit("ledger task must be PLAN or an AFV2 task; history is read-only")
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
    ss.add_argument("--pr", action="append", help="repeat once per PR (multi-repository tasks)")
    ss.add_argument("--merge", action="append", help="REPO@SHA; repeat once per repository")
    ss.add_argument("--publication", action="append", help="repeat once per publication or deployment")
    ss.add_argument("--reason")
    ss.add_argument("--blocked-by", help="comma-separated H- or AR- IDs from the acceptance register")
    lg = sub.add_parser("ledger")
    lg.add_argument("task")
    lg.add_argument("kind")
    lg.add_argument("text")
    args = ap.parse_args(argv)
    graph = load()
    if args.cmd != "validate" and graph.get("schema") != 3:
        raise SystemExit("commands require the current schema-3 graph; history is read-only")
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
        blocked_by = [x.strip() for x in args.blocked_by.split(",") if x.strip()] if args.blocked_by else None
        set_state(graph, args.task, args.state, args.pr, args.merge, args.publication, args.reason, blocked_by)
        errors = validate(graph)
        if errors:
            raise SystemExit("state change was not saved: " + "; ".join(errors))
        save(graph)
        SEQUENCE.write_text(render_sequence(graph), encoding="utf-8", newline="\n")
        print(f"{args.task} -> {args.state}")
        return 0
    if args.cmd == "ledger":
        if args.task != "PLAN" and args.task not in {t["id"] for t in graph["tasks"]}:
            raise SystemExit(f"unknown current task {args.task}")
        print(json.dumps(ledger_append(args.task, args.kind, args.text)))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
