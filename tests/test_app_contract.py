from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

class BrowserAppContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = (ROOT / "app.js").read_text(encoding="utf-8")
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")

    def test_runtime_hardening(self):
        self.assertIn("try{persisted=JSON.parse", self.app)
        self.assertIn("async function getJSON", self.app)
        self.assertIn("!r.ok", self.app)

    def test_core_workflow_contract(self):
        for token in ["scoreAlert", "scoreAI", "mlFeatures", "hybrid_risk", "model_version", "caseForAlert", "renderPlaybooks", "renderMitre", "openAlert", "openIncident", "localStorage"]:
            self.assertIn(token, self.app)

    def test_security_contract(self):
        csp = re.search(r'Content-Security-Policy[^>]+', self.html)
        self.assertIsNotNone(csp)
        self.assertIn("object-src 'none'", csp.group(0))
        self.assertIn("frame-ancestors 'none'", csp.group(0))
        self.assertNotIn("http://", self.app)
        self.assertNotIn("https://", self.app)
        self.assertIn('./ai_engine/model.json', self.app)

if __name__ == "__main__":
    unittest.main()
