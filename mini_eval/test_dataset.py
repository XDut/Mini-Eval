import json
from pathlib import Path

def test_dataset_is_balanced_and_complete():
    rows = [json.loads(x) for x in Path(__file__).with_name("questions.jsonl").read_text().splitlines()]
    assert len(rows) == 24
    assert len({r['id'] for r in rows}) == 24
    assert sum(r['kind'] == 'answerable' for r in rows) == 12
    assert sum(r['kind'] == 'unanswerable' for r in rows) == 12
    assert all(r['guidance'] for r in rows)
