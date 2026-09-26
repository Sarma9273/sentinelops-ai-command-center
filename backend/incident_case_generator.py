
"""
SentinelOps-AI Incident Case Generator

Purpose:
Convert high-risk SOC/SIEM alerts into structured incident cases.

This file is generated from Phase 1.3.
"""

from datetime import datetime


def should_create_incident(alert):
    score = int(alert.get("ai_risk_score", 0))
    risk_level = str(alert.get("ai_risk_level", "")).lower()
    severity = str(alert.get("severity", "")).lower()

    return score >= 65 or risk_level in ["high", "critical"] or severity in ["high", "critical"]


def create_case_id(alert):
    alert_id = alert.get("alert_id", "UNKNOWN")
    return f"INC-{alert_id.replace('ALERT-', '')}"


def decide_priority(alert):
    score = int(alert.get("ai_risk_score", 0))

    if score >= 85:
        return "P1 - Critical"
    elif score >= 65:
        return "P2 - High"
    elif score >= 35:
        return "P3 - Medium"
    return "P4 - Low"


def create_incident_from_alert(alert):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "case_id": create_case_id(alert),
        "linked_alert_id": alert.get("alert_id"),
        "created_at": now,
        "updated_at": now,
        "case_title": alert.get("rule_name", "Security Alert Investigation"),
        "case_status": "Open",
        "priority": decide_priority(alert),
        "severity": alert.get("ai_risk_level", alert.get("severity", "Unknown")),
        "ai_risk_score": alert.get("ai_risk_score"),
        "incident_type": alert.get("event_type", "unknown"),
        "affected_host": alert.get("target_host", "-"),
        "source_ip": alert.get("source_ip", "-"),
        "username": alert.get("username", "-"),
        "mitre_id": alert.get("mitre_id", "-"),
        "mitre_tactic": alert.get("mitre_tactic", "-"),
        "mitre_technique": alert.get("mitre_technique", "-"),
        "soc_decision": alert.get("soc_decision", "-"),
        "recommended_action": alert.get("recommended_action", "-"),
        "ai_explanation": alert.get("ai_explanation", "-"),
        "assigned_to": "SOC L1 Analyst",
        "analyst_notes": "",
        "final_verdict": "Pending"
    }
