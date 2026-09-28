"""Train the local SentinelOps-AI logistic risk model without third-party runtime dependencies."""
import json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"ai_engine/training_data.json"
MODEL=ROOT/"ai_engine/model.json"

def sigmoid(z):
    z=max(-30.0,min(30.0,z))
    return 1.0/(1.0+math.exp(-z))

def train(rows, epochs=8000, learning_rate=0.5, l2=0.1):
    x=[r["features"] for r in rows]
    y=[r["label"] for r in rows]
    n=len(x); d=len(x[0]); w=[0.0]*(d+1)
    for _ in range(epochs):
        g=[0.0]*(d+1)
        for features,label in zip(x,y):
            p=sigmoid(w[0]+sum(w[i+1]*features[i] for i in range(d)))
            error=p-label
            g[0]+=error
            for i in range(d):
                g[i+1]+=error*features[i]
        for i in range(d+1):
            g[i]/=n
            if i: g[i]+=l2*w[i]
            w[i]-=learning_rate*g[i]
    return w

def main():
    payload=json.loads(DATA.read_text(encoding="utf-8"))
    weights=train(payload["rows"])
    model=json.loads(MODEL.read_text(encoding="utf-8"))
    model["intercept"]=round(weights[0],8)
    model["coefficients"]=[round(v,8) for v in weights[1:]]
    MODEL.write_text(json.dumps(model,indent=2)+"\n",encoding="utf-8")
    print("Model trained:",MODEL)

if __name__=="__main__":
    main()
