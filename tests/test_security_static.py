from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

class StaticSecurityAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = (ROOT / "app.js").read_text(encoding="utf-8")
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")

    def test_no_dynamic_code_execution(self):
        for pattern in [r"\beval\s*\(", r"\bnew\s+Function\s*\(", r"\bFunction\s*\("]:
            self.assertIsNone(re.search(pattern, self.app))

    def test_no_document_write_or_external_runtime(self):
        self.assertNotIn("document.write", self.app)
        self.assertNotIn("http://", self.app)
        self.assertNotIn("https://", self.app)

    def test_required_csp_controls(self):
        csp = re.search(r'Content-Security-Policy[^>]+', self.html)
        self.assertIsNotNone(csp)
        value = csp.group(0)
        for directive in ["default-src 'self'", "script-src 'self'", "object-src 'none'", "base-uri 'self'", "form-action 'self'"]:
            self.assertIn(directive, value)

    def test_dynamic_html_uses_escaping_for_known_untrusted_fields(self):
        for raw in ['data-alert="\${a.alert_id}"', 'data-incident="\${i.case_id}"', 'data-create-case="\${a.alert_id}"', '\${x.alerts.join(", ")}']:
            self.assertNotIn(raw, self.app)

    def test_local_state_is_browser_only(self):
        self.assertIn("localStorage", self.app)
        self.assertIn('fetch("./sample_data/alerts_sample.json"', self.app)
        self.assertIn('fetch("./ai_engine/model.json"', self.app)

if __name__ == "__main__":
    unittest.main()
