"""Evaluate the committed local logistic model on a deterministic holdout split."""
import json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/"ai_engine/training_data.json").read_text())
model=json.loads((ROOT/"ai_engine/model.json").read_text())
rows=data["rows"]
cut=int(len(rows)*0.8)
train, test=rows[:cut], rows[cut:]

def sigmoid(z):
    return 1/(1+math.exp(-max(-30,min(30,z))))

def predict(features):
    z=model["intercept"]+sum(c*x for c,x in zip(model["coefficients"],features))
    return sigmoid(z)

tp=tn=fp=fn=0
for row in test:
    pred=1 if predict(row["features"])>=.5 else 0
    if pred==1 and row["label"]==1: tp+=1
    elif pred==0 and row["label"]==0: tn+=1
    elif pred==1: fp+=1
    else: fn+=1
precision=tp/(tp+fp) if tp+fp else 0
recall=tp/(tp+fn) if tp+fn else 0
f1=2*precision*recall/(precision+recall) if precision+recall else 0
accuracy=(tp+tn)/len(test) if test else 0
fpr=fp/(fp+tn) if fp+tn else 0
result={"model":model["model_name"],"model_version":model["model_version"],"test_rows":len(test),"true_positive":tp,"true_negative":tn,"false_positive":fp,"false_negative":fn,"precision":round(precision,4),"recall":round(recall,4),"f1":round(f1,4),"accuracy":round(accuracy,4),"false_positive_rate":round(fpr,4)}
print(json.dumps(result,indent=2))
