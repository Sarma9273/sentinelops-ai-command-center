import json, unittest
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from correlation.correlation_engine import correlate

class V2ModuleTests(unittest.TestCase):
 def test_correlation_groups_related_alerts(self):
  alerts=[
   {"alert_id":"A1","source_ip":"10.0.0.1","target_host":"h1","username":"u","mitre_id":"T1"},
   {"alert_id":"A2","source_ip":"10.0.0.1","target_host":"h2","username":"v","mitre_id":"T2"},
   {"alert_id":"A3","source_ip":"10.0.0.2","target_host":"h3","username":"z","mitre_id":"T3"}]
  groups=correlate(alerts)
  self.assertEqual(groups[0]["count"],2)
  self.assertEqual(groups[1]["count"],1)
 def test_contract_files(self):
  for p in ["correlation/correlation_rules.json","workflow/alert_lifecycle.json"]:
   with open(ROOT/p,encoding="utf-8") as f: json.load(f)

if __name__=="__main__": unittest.main()
