# Current V2 ledger

Only PLAN notes and current AFV2 task records belong in [ledger.jsonl](ledger.jsonl). The pre-V2 ledger is preserved unchanged in [history](../history/v1-20261114/ledger/ledger.jsonl). The coordinator appends via tools/plan.py; never rewrite old entries or copy completed history into current task states.

Design migration records establish source and scope, not product implementation authorization. A future user-authorized range must be recorded before the first task starts. Delivered records include each exact PR/merge and ordinary publication identity; missing native proof remains explicit.
