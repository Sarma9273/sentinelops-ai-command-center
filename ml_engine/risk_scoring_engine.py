
from collections import Counter

class RiskScoringEngine:
    def __init__(self, alerts):
        self.alerts = alerts
        self.source_ip_counter = Counter(
            alert.get("source_ip")
            for alert in alerts
            if alert.get("source_ip") and alert.get("source_ip") != "-"
        )

    def calculate_score(self, alert):
        score = 0
        reasons = []

        rule_level = int(alert.get("rule_level", 0))
        score += rule_level * 7
        reasons.append(f"Rule level {rule_level} contributed {rule_level * 7} points.")

        severity = str(alert.get("severity", "")).lower()
        severity_points = {"critical": 20, "high": 15, "medium": 8, "low": 3}

        if severity in severity_points:
            score += severity_points[severity]
            reasons.append(f"{severity.title()} severity contributed {severity_points[severity]} points.")

        if alert.get("successful_login_after_failures") is True:
            score += 15
            reasons.append("Successful login after failures increased risk.")

        failed_attempts = int(alert.get("failed_attempts", 0))

        if failed_attempts >= 100:
            score += 15
        elif failed_attempts >= 50:
            score += 10
        elif failed_attempts >= 10:
            score += 5

        mitre_tactic = str(alert.get("mitre_tactic", "")).lower()

        if mitre_tactic in ["credential access", "privilege escalation", "persistence", "defense evasion", "exfiltration", "command and control"]:
            score += 10
        elif mitre_tactic in ["discovery", "reconnaissance", "initial access", "execution"]:
            score += 5

        source_ip = alert.get("source_ip", "-")
        source_ip_count = self.source_ip_counter.get(source_ip, 0)

        if source_ip_count >= 3:
            score += 10
        elif source_ip_count == 2:
            score += 5

        event_type = str(alert.get("event_type", "")).lower()

        if event_type == "privilege_escalation":
            score += 15
        elif event_type == "authentication_failure":
            score += 8
        elif event_type == "network_scan":
            score += 5

        return min(score, 100), reasons

    def assign_risk_level(self, score):
        if score >= 85:
            return "Critical"
        elif score >= 65:
            return "High"
        elif score >= 35:
            return "Medium"
        return "Low"

    def enrich_all_alerts(self):
        enriched_alerts = []

        for alert in self.alerts:
            score, reasons = self.calculate_score(alert)
            risk_level = self.assign_risk_level(score)

            enriched = alert.copy()
            enriched["ai_risk_score"] = score
            enriched["ai_risk_level"] = risk_level
            enriched["risk_reasons"] = reasons

            enriched_alerts.append(enriched)

        return enriched_alerts
