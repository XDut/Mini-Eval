"""Inspect AI task using locally running Hugging Face models (no API)."""
import json
import sys
from pathlib import Path
from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import Score, Scorer, Target, scorer, accuracy, stderr
from inspect_ai.solver import generate
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from shared.scoring import mini_score
DATA=Path(__file__).with_name('questions.jsonl')

def load_samples():
    samples=[]
    for line in DATA.read_text(encoding='utf-8').splitlines():
        if not line.strip():continue
        row=json.loads(line)
        prompt=('Answer accurately. If the answer cannot be known, state that clearly. '
                'Do not invent private or future facts.\n\nQuestion: '+row['input'])
        samples.append(Sample(id=row['id'],input=prompt,target=row['target'],metadata=row))
    return samples

@scorer(metrics=[accuracy(),stderr()])
def answerability_scorer()->Scorer:
    async def score(state, target: Target)->Score:
        row=state.metadata
        answer=state.output.completion
        verdict=mini_score(row,answer)
        return Score(value=1.0 if verdict['correct'] else 0.0,answer=answer,
                     explanation=f"{row['kind']}; abstained={verdict['abstained']}; target={row['target']!r}; lexical heuristic; audit manually",
                     metadata={'kind':row['kind'],**verdict})
    return score

@task
def uncertainty_mini_eval():
    return Task(dataset=load_samples(),solver=generate(),scorer=answerability_scorer())
