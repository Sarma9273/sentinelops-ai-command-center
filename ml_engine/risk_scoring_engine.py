from collections import Counter


class RiskScoringEngine:
    """Deterministic, explainable risk scorer used by the Phase 1 reference layer."""

    HIGH_RISK_TACTICS = {
        "credential access",
        "privilege escalation",
        "persistence",
        "defense evasion",
        "exfiltration",
        "command and control",
    }
    MODERATE_RISK_TACTICS = {
        "discovery",
        "reconnaissance",
        "initial access",
        "execution",
    }

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
        points = rule_level * 7
        score += points
        reasons.append(f"Rule level {rule_level} contributed {points} points.")

        severity = str(alert.get("severity", "")).lower()
        severity_points = {"critical": 20, "high": 15, "medium": 8, "low": 3}
        if severity in severity_points:
            points = severity_points[severity]
            score += points
            reasons.append(
                f"{severity.title()} severity contributed {points} points."
            )

        if alert.get("successful_login_after_failures") is True:
            score += 15
            reasons.append("Successful login after failures increased risk.")

        failed_attempts = int(alert.get("failed_attempts", 0))
        if failed_attempts >= 100:
            points = 15
        elif failed_attempts >= 50:
            points = 10
        elif failed_attempts >= 10:
            points = 5
        else:
            points = 0
        if points:
            score += points
            reasons.append(
                f"Failed-attempt volume contributed {points} points."
            )

        mitre_tactic = str(alert.get("mitre_tactic", "")).lower()
        if mitre_tactic in self.HIGH_RISK_TACTICS:
            score += 10
            reasons.append(
                f"High-risk MITRE tactic '{alert.get('mitre_tactic')}' contributed 10 points."
            )
        elif mitre_tactic in self.MODERATE_RISK_TACTICS:
            score += 5
            reasons.append(
                f"MITRE tactic '{alert.get('mitre_tactic')}' contributed 5 points."
            )

        source_ip = alert.get("source_ip", "-")
        source_ip_count = self.source_ip_counter.get(source_ip, 0)
        if source_ip_count >= 3:
            points = 10
        elif source_ip_count == 2:
            points = 5
        else:
            points = 0
        if points:
            score += points
            reasons.append(
                f"Source IP {source_ip} repetition contributed {points} points."
            )

        event_type = str(alert.get("event_type", "")).lower()
        event_points = {
            "privilege_escalation": 15,
            "authentication_failure": 8,
            "network_scan": 5,
        }
        if event_type in event_points:
            points = event_points[event_type]
            score += points
            reasons.append(
                f"Event type '{event_type}' contributed {points} points."
            )

        return min(score, 100), reasons

    def assign_risk_level(self, score):
        if score >= 85:
            return "Critical"
        if score >= 65:
            return "High"
        if score >= 35:
            return "Medium"
        return "Low"

    def enrich_all_alerts(self):
        enriched_alerts = []
        for alert in self.alerts:
            score, reasons = self.calculate_score(alert)
            enriched = alert.copy()
            enriched["ai_risk_score"] = score
            enriched["ai_risk_level"] = self.assign_risk_level(score)
            enriched["risk_reasons"] = reasons
            enriched_alerts.append(enriched)
        return enriched_alerts
