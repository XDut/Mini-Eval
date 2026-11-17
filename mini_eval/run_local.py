"""Run locally; only writes real model results (never simulated metrics)."""
import argparse,csv,json,sys,time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from shared.scoring import mini_score,stratified,summarize_mini
from shared.hf_model import ModelClient
BASE=Path(__file__).resolve().parent
SYSTEM='Answer accurately. If you cannot know an answer, state that clearly. Do not invent facts.'

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--model',default='Qwen/Qwen2.5-0.5B-Instruct')
    parser.add_argument('--limit',type=int,default=0,help='0 = all 24; smaller values are stratified')
    parser.add_argument('--seed',type=int,default=42)
    parser.add_argument('--temperature',type=float,default=0.)
    args=parser.parse_args()
    if args.limit<0 or not 0<=args.temperature<=1:parser.error('Invalid limit or temperature')
    items=[json.loads(s) for s in (BASE/'questions.jsonl').read_text(encoding='utf8').splitlines() if s.strip()]
    items=stratified(items,args.limit,'kind',args.seed)
    model=ModelClient(args.model)
    results=[]
    for i,item in enumerate(items,1):
        result={**item,'model':model.model,'temperature':args.temperature,'answer':'','manual_label':'unreviewed','error':''}
        try:
            result['answer']=model.generate(SYSTEM,'Question: '+item['input'],args.temperature)
            result.update(mini_score(item,result['answer']))
        except Exception as exc:
            result.update({'correct':False,'abstained':False,'verdict':'error','error':str(exc)})
        results.append(result)
        print(f'{i}/{len(items)} {item["id"]} {result["verdict"]}',flush=True)
    out=BASE/'results';out.mkdir(exist_ok=True)
    stamp=time.strftime('%Y%m%d-%H%M%S')
    with (out/f'trials-{stamp}.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(results[0]));w.writeheader();w.writerows(results)
    report={'model':args.model,'seed':args.seed,'temperature':args.temperature,'source':'actual local-model generations',**summarize_mini(results)}
    (out/f'results-{stamp}.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
