# Ledger

`ledger.jsonl` is append-only: one JSON object per line, `{at, task, kind, text}`.
- `at` is UTC ISO-8601.
- `kind` is one of `plan`, `started`, `delivered`, `complete`, `superseded` or `note`.

Records are written only with `python tools/plan.py ledger <task> <kind> "<text>"` and committed through a Plan PR. Graph states (`delivery-graph.json`) carry the evidence (PRs, merges, publications); the ledger carries the narrative. Never rewrite or delete a line. Corrections are new `note` lines.
