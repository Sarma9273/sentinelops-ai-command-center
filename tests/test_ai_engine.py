import json, math, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class TestAIEngine(unittest.TestCase):
    def test_training_contract(self):
        data=json.loads((ROOT/"ai_engine/training_data.json").read_text())
        self.assertEqual(len(data["rows"]),80)
        self.assertEqual({r["label"] for r in data["rows"]},{0,1})
        self.assertEqual(len(data["feature_order"]),8)
        self.assertTrue(all(len(r["features"])==8 for r in data["rows"]))
        self.assertTrue(all(0.0 <= v <= 1.0 for r in data["rows"] for v in r["features"]))

    def test_model_contract(self):
        model=json.loads((ROOT/"ai_engine/model.json").read_text())
        self.assertEqual(model["model_version"],"1.1.0")
        self.assertEqual(model["algorithm"],"logistic_regression")
        self.assertEqual(len(model["feature_order"]),8)
        self.assertEqual(len(model["coefficients"]),8)
        p=1/(1+math.exp(-(model["intercept"]+sum(c*x for c,x in zip(model["coefficients"],[1]*8)))))
        self.assertGreaterEqual(p,0.0)
        self.assertLessEqual(p,1.0)

if __name__=="__main__":
    unittest.main()
