import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ProjectIntegrityTests(unittest.TestCase):
    def test_required_runtime_files(self):
        for rel in [
            "index.html",
            "styles.css",
            "app.js",
            "sample_data/alerts_sample.json",
            "database/incidents_db.json",
            "incident_playbooks/default_soc_playbooks.json",
        ]:
            self.assertTrue((ROOT / rel).is_file(), rel)

    def test_json_data_contracts(self):
        for rel in [
            "sample_data/alerts_sample.json",
            "sample_data/alerts_enriched_with_risk.json",
            "database/incidents_db.json",
            "incident_playbooks/default_soc_playbooks.json",
            "project_manifest.json",
        ]:
            with self.subTest(rel=rel):
                with open(ROOT / rel, encoding="utf-8") as f:
                    json.load(f)

    def test_risk_engine_expected_scores(self):
        import sys
        sys.path.insert(0, str(ROOT))
        from ml_engine.risk_scoring_engine import RiskScoringEngine

        with open(ROOT / "sample_data/alerts_sample.json", encoding="utf-8") as f:
            alerts = json.load(f)
        enriched = RiskScoringEngine(alerts).enrich_all_alerts()
        self.assertEqual([a["ai_risk_score"] for a in enriched], [100, 67, 100])
        self.assertEqual([a["ai_risk_level"] for a in enriched], ["Critical", "High", "Critical"])

    def test_incident_generation_contract(self):
        import sys
        sys.path.insert(0, str(ROOT))
        from backend.incident_case_generator import (
            should_create_incident,
            create_incident_from_alert,
        )

        with open(ROOT / "sample_data/alerts_enriched_with_risk.json", encoding="utf-8") as f:
            alerts = json.load(f)
        for alert in alerts:
            self.assertTrue(should_create_incident(alert))
            case = create_incident_from_alert(alert)
            self.assertEqual(case["linked_alert_id"], alert["alert_id"])
            self.assertTrue(case["case_id"].startswith("INC-"))


if __name__ == "__main__":
    unittest.main()
